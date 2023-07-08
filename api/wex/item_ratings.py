"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles all the item ratings requests
"""
import os
import urllib.parse

import sanic

from utils.sanic_gzip import Compress
from utils.utils import authorized as auth

compress = Compress()
wex_item_ratings = sanic.Blueprint("wex_item_ratings")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/item_ratings/accountId/templateId.md
@wex_item_ratings.route("/api/game/v2/item_ratings/<accountId>/<templateId>", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def item_ratings(request: sanic.request.Request, accountId: str, templateId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to get item ratings from the server
    :param request: The request object
    :param accountId: The account id
    :param templateId: The template id
    :return: The response object (204)
    """
    my_rating = {
        "gameplayRating": 0,
        "appearanceRating": 0
    }
    data = await request.app.ctx.read_file(f"res/wex/api/game/v2/item_ratings/{accountId}.json")
    template_id = urllib.parse.unquote(templateId)
    character_datatable = await request.app.ctx.load_datatable("Content/Characters/Datatables/CharacterStats")
    rating_key = character_datatable[0]["Rows"].get(f"CD.{template_id.split(':')[1].replace('_', '.')}", {}).get(
        "RatingsKey", f"CD.{template_id.split(':')[1].replace('_', '.')}")
    if rating_key in data:
        my_rating = data[rating_key]
    overall_ratings = await request.app.ctx.read_file("res/wex/api/game/v2/item_ratings/ratings.json")
    ratings = []
    if rating_key in overall_ratings:
        for rating in overall_ratings[rating_key]:
            ratings.append({
                "gameplayRating": rating[0],
                "appearanceRating": rating[1]
            })
    else:
        ratings = [{
            "gameplayRating": 0,
            "appearanceRating": 0
        }, {
            "gameplayRating": 0,
            "appearanceRating": 0
        }, {
            "gameplayRating": 0,
            "appearanceRating": 0
        }, {
            "gameplayRating": 0,
            "appearanceRating": 0
        }, {
            "gameplayRating": 0,
            "appearanceRating": 0
        }]
    for file in os.listdir("res/wex/api/game/v2/item_ratings"):
        if file == "ratings.json":
            continue
        user_data = await request.app.ctx.read_file(f"res/wex/api/game/v2/item_ratings/{file}")
        if rating_key in user_data and user_data[rating_key]["gameplayRating"] != 0:
            ratings[user_data[rating_key]["gameplayRating"] - 1]["gameplayRating"] += 1
            ratings[user_data[rating_key]["appearanceRating"] - 1]["appearanceRating"] += 1
    return sanic.response.json({
        "myRating": my_rating,
        "overallRatings": {
            "ratingsKey": rating_key,
            "discussUrl": "https://discord.gg/stw-dailies-757765475823517851",
            "ratings": ratings
        }
    })


# undocumented
@wex_item_ratings.route("/api/game/v2/item_ratings/<accountId>/<templateId>", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def set_item_rating(request: sanic.request.Request, accountId: str,
                          templateId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to rate an item
    :param request: The request object
    :param accountId: The account id
    :param templateId: The template id
    :return: The response object (204)
    """
    data = await request.app.ctx.read_file(f"res/wex/api/game/v2/item_ratings/{accountId}.json")
    template_id = urllib.parse.unquote(templateId)
    character_datatable = await request.app.ctx.load_datatable("Content/Characters/Datatables/CharacterStats")
    rating_key = character_datatable[0]["Rows"].get(f"CD.{template_id.split(':')[1].replace('_', '.')}", {}).get(
        "RatingsKey", f"CD.{template_id.split(':')[1].replace('_', '.')}")
    data[rating_key] = {
        "gameplayRating": request.json["gameplayRating"],
        "appearanceRating": request.json["appearanceRating"]
    }
    if data[rating_key]["gameplayRating"] > 5:
        data[rating_key]["gameplayRating"] = 5
    if data[rating_key]["appearanceRating"] > 5:
        data[rating_key]["appearanceRating"] = 5
    await request.app.ctx.write_file(f"res/wex/api/game/v2/item_ratings/{accountId}.json", data)
    overall_ratings = await request.app.ctx.read_file("res/wex/api/game/v2/item_ratings/ratings.json")
    ratings = []
    if rating_key in overall_ratings:
        for rating in overall_ratings[rating_key]:
            ratings.append({
                "gameplayRating": rating[0],
                "appearanceRating": rating[1]
            })
    else:
        ratings = [{
            "gameplayRating": 0,
            "appearanceRating": 0
        }, {
            "gameplayRating": 0,
            "appearanceRating": 0
        }, {
            "gameplayRating": 0,
            "appearanceRating": 0
        }, {
            "gameplayRating": 0,
            "appearanceRating": 0
        }, {
            "gameplayRating": 0,
            "appearanceRating": 0
        }]
    for file in os.listdir("res/wex/api/game/v2/item_ratings"):
        if file == "ratings.json":
            continue
        user_data = await request.app.ctx.read_file(f"res/wex/api/game/v2/item_ratings/{file}")
        if rating_key in user_data and user_data[rating_key]["gameplayRating"] != 0:
            ratings[user_data[rating_key]["gameplayRating"] - 1]["gameplayRating"] += 1
            ratings[user_data[rating_key]["appearanceRating"] - 1]["appearanceRating"] += 1
    return sanic.response.json({
        "myRating": {
            "gameplayRating": request.json["gameplayRating"],
            "appearanceRating": request.json["appearanceRating"]
        },
        "overallRatings": {
            "ratingsKey": rating_key,
            "discussUrl": "https://discord.gg/stw-dailies-757765475823517851",
            "ratings": ratings
        }
    })
