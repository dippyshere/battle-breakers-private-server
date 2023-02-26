"""
A Battle Breakers Private server written in Python by Dippyshere
https://github.com/Dippyshere/Battle-Breakers-Private-Server
"""

from api import api

import orjson
import sanic
import colorama

try:
    import tomllib as toml
except ModuleNotFoundError:
    import tomli as toml

colorama.init()

app = sanic.app.Sanic('dippy_breakers', dumps=orjson.dumps, loads=orjson.loads)
app.blueprint(api)

with open("config.toml", "rb") as config_file:
    config = toml.load(config_file)
    config_file.close()


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/QueryProfile?profileId=profile0&rvn=-1
@app.route("/wex/api/game/v2/profile/<accountId>/QueryProfile", methods=["POST"])
async def query_profile(request, accountId: str):
    """
    Handles the query profile request
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    with open(f"res/wex/api/game/v2/profile/{accountId}/QueryProfile/{request.args.get('profileId')}.json",
              "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/ClaimLoginReward?profileId=profile0&rvn=9999
@app.route("/wex/api/game/v2/profile/<accountId>/ClaimLoginReward", methods=["POST"])
async def claim_login_reward(request, accountId: str):
    """
    Handles the daily reward request
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json({
        "profileRevision": 40315,
        "profileId": "profile0",
        "profileChangesBaseRevision": 40314,
        "profileChanges": [{
            "changeType": "itemQuantityChanged",
            "itemId": "03e1d076-957e-43f2-9702-71d521413717",
            "quantity": 501
        }, {
            "changeType": "statModified",
            "name": "login_reward",
            "value": {
                "last_claim_time": "2022-12-29T05:43:30.806Z",
                "next_level": 187
            }
        }, {
            "changeType": "statModified",
            "name": "hammer_quest_energy",
            "value": {
                "energy_spent": 0,
                "energy_required": 100,
                "claim_count": 0
            }
        }, {
            "changeType": "statModified",
            "name": "activity",
            "value": {
                "a": {
                    "date": "2022-12-28T00:00:00.000Z",
                    "claimed": False,
                    "props": {
                        "HeroAcquired": 137,
                        "HeroPromote": 1,
                        "HeroEvolve": 1,
                        "MonsterPitLevelUp": 1,
                        "HeroFoil": 1,
                        "AccountLevelUp": 2,
                        "BaseBonus": 10,
                        "EnergySpent": 187
                    }
                },
                "b": {
                    "date": "2022-12-29T00:00:00.000Z",
                    "claimed": False,
                    "props": {
                        "BaseBonus": 10
                    }
                },
                "standardGift": 10
            }
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "f7c3b0c5-d208-4bc4-b6d5-054359784dd0",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "7b899484-837c-4eea-aa0d-a80ce97ae0d7",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "7585df88-2a1e-4ca4-b0ce-33ab0aaac483",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "88721a32-4602-46eb-9662-294610e2e7b5",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "ef81e090-a854-48fd-8924-ef7d07eb0301",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "b8ef336b-e07a-4c41-9b8c-5544746d55d6",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "9b0fffd3-92f3-4018-9799-0bd89c6804c3",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "b83d82de-0cd3-4eac-8cb5-9cfec3360853",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "8b1d13e5-6ee3-4265-96a8-c3e62646a87d",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "dff1fe19-d477-4249-8e2d-258c0df83c78",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "ab0cd5f2-2a8f-47df-8470-0de41c526669",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "881eefbe-f2a5-4646-abb3-c3b74500e94b",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "96f38f41-74dd-4483-a65c-89f2926bd399",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "157e63f4-ba1e-4b3e-9852-bc03eb70087d",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "67ef7c06-d6a8-46fa-9b97-3aa7ea7eca5b",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "37434995-4e63-4c10-ad4c-d19342ed1caa",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "f312dfdf-6d50-42ed-898f-024e45726e7a",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "ac2854b7-ecb2-4451-b683-ff303e98b605",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "517052fe-383b-4c69-97ef-2a7c850e6429",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "ebcfcb8e-7e70-4e05-a0a5-e50b561158d2",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "d922c670-e4c9-4b84-9601-c5f9ec5f3a87",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "b545182f-9443-4a03-a212-95b7d6083067",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "c97235e4-3aab-499c-8b45-9b0c0a2e9a4b",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "e213cc8c-7356-40f7-bef6-9fbadc44efc7",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "1221e7d1-1852-4e8e-9d15-bc29255abb1d",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "372c4622-1b84-4c48-980e-9c42b03ca30b",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "68686864-8ba4-460c-9d89-a7e6b95309ba",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "58c04ea5-b601-4af4-ab83-0e89b7387e15",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "d59ca1b7-3ce9-4053-956b-44d4c0977500",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "cbc1e014-8d1f-434d-8a6b-34bb6128eb4a",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "04535e24-3fb5-4e77-b188-8cf979da47ef",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "736887db-c0b6-459f-af0a-4e6d6a568de2",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "f25baf81-2fc3-4e2d-940b-b50453ade9c0",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }],
        "profileCommandRevision": 24007,
        "serverTime": "2022-12-29T05:43:30.810Z",
        "responseVersion": 1
    })


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SendGiftPoints?profileId=profile0&rvn=99999
@app.route("/wex/api/game/v2/profile/<accountId>/SendGiftPoints", methods=["POST"])
async def send_gift_points(request, accountId: str):
    """
    Handles the send gift point request
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json({
        "profileRevision": 39840,
        "profileId": "profile0",
        "profileChangesBaseRevision": 39838,
        "profileChanges": [{
            "changeType": "statModified",
            "name": "activity",
            "value": {
                "a": {
                    "date": "2022-12-28T00:00:00.000Z",
                    "claimed": False,
                    "props": {
                        "BaseBonus": 10
                    }
                },
                "b": {
                    "date": "2022-12-27T00:00:00.000Z",
                    "claimed": True,
                    "props": {
                        "BaseBonus": 10,
                        "EnergySpent": 3
                    }
                },
                "standardGift": 10
            }
        }],
        "profileCommandRevision": 23699,
        "serverTime": "2022-12-28T11:37:06.741Z",
        "multiUpdate": [{
            "profileRevision": 9864,
            "profileId": "friends",
            "profileChangesBaseRevision": 9862,
            "profileChanges": [],
            "profileCommandRevision": 8247
        }],
        "responseVersion": 1
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8889, auto_reload=True)
