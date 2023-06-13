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


# https://github.com/dippyshere/battle-breakers-documentation/tree/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/item_ratings/ec0ebb7e56f6454e86c62299a7b32e21
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
    templateId = urllib.parse.unquote(templateId)
    if templateId in data:
        my_rating = data[templateId]
    character_datatable = await request.app.ctx.load_datatable("Content/Characters/Datatables/CharacterStats")
    rating_key = character_datatable[0]["Rows"].get(f"CD.{templateId.split(':')[1].replace('_', '.')}", {}).get(
        "RatingsKey", f"CD.{templateId.split(':')[1].replace('_', '.')}")
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
        if templateId in user_data and user_data[templateId]["gameplayRating"] != 0:
            ratings[user_data[templateId]["gameplayRating"] - 1]["gameplayRating"] += 1
            ratings[user_data[templateId]["appearanceRating"] - 1]["appearanceRating"] += 1
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
    templateId = urllib.parse.unquote(templateId)
    data[templateId] = {
        "gameplayRating": request.json["gameplayRating"],
        "appearanceRating": request.json["appearanceRating"]
    }
    if data[templateId]["gameplayRating"] > 5:
        data[templateId]["gameplayRating"] = 5
    if data[templateId]["appearanceRating"] > 5:
        data[templateId]["appearanceRating"] = 5
    await request.app.ctx.write_file(f"res/wex/api/game/v2/item_ratings/{accountId}.json", data)
    character_datatable = await request.app.ctx.load_datatable("Content/Characters/Datatables/CharacterStats")
    rating_key = character_datatable[0]["Rows"].get(f"CD.{templateId.split(':')[1].replace('_', '.')}", {}).get(
        "RatingsKey", f"CD.{templateId.split(':')[1].replace('_', '.')}")
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
        if templateId in user_data and user_data[templateId]["gameplayRating"] != 0:
            ratings[user_data[templateId]["gameplayRating"] - 1]["gameplayRating"] += 1
            ratings[user_data[templateId]["appearanceRating"] - 1]["appearanceRating"] += 1
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
