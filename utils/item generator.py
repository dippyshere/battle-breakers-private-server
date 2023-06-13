"""
Handy utility to generate item templates to paste into a profile
input is something like:
WorldExplorers/Content/Characters/Classes/MartialArtist/Multi_TripleCombo/CD_MartialArtist_SR2_Dark_TripleCombo_T06
WorldExplorers/Content/Characters/Classes/Archer/Multi_PenetratingShot/CD_Archer_SR2_Dark_PenetratingShot_T06

output is something like:
{"f01dfe95-6a2c-4a18-a3d9-19709c5f7de1":{"templateId":"Character:MartialArtist_SR2_Dark_TripleCombo_T06","attributes":{"gear_weapon_item_id":"","weapon_unlocked":true,"sidekick_template_id":"","level":150,"is_new":true,"num_sold":0,"skill_level":20,"sidekick_unlocked":true,"upgrades":[95,95,95,95,34,75,3,65,3],"gear_armor_item_id":"","used_as_sidekick":false,"skill_xp":0,"armor_unlocked":true,"foil_lvl":-1,"xp":0,"rank":10,"sidekick_item_id":""},"quantity":1}{"ef06177e-f547-4092-8a19-96200f440740":{"templateId":"Character:Archer_SR2_Dark_PenetratingShot_T06","attributes":{"gear_weapon_item_id":"","weapon_unlocked":true,"sidekick_template_id":"","level":150,"is_new":true,"num_sold":0,"skill_level":20,"sidekick_unlocked":true,"upgrades":[95,95,95,95,34,75,3,65,3],"gear_armor_item_id":"","used_as_sidekick":false,"skill_xp":0,"armor_unlocked":true,"foil_lvl":-1,"xp":0,"rank":10,"sidekick_item_id":""},"quantity":1}
"""

import uuid
import json


def generate_item_template(item_path: str) -> dict:
    if item_path[-1] == "6" or item_path[-1] == "7" or item_path[-1] == "8" or item_path[-1] == "9":
        level = 150
    else:
        level = 120
    return {
        str(uuid.uuid4()):
            {
                "templateId": f"Character:{item_path[3:]}",
                "attributes": {
                    "gear_weapon_item_id": "", "weapon_unlocked": False, "sidekick_template_id": "", "level": level,
                    "is_new": True, "num_sold": 0, "skill_level": 20, "sidekick_unlocked": False,
                    "upgrades": [95, 95, 95, 95, 34, 75, 3, 65, 3], "gear_armor_item_id": "", "used_as_sidekick": False,
                    "skill_xp": 0, "armor_unlocked": True, "foil_lvl": -1, "xp": 0, "rank": 10, "sidekick_item_id": ""
                },
                "quantity": 1
            }
    }


def generate_item_templates(item_paths: list) -> str:
    templates = ""
    for item_path in item_paths:
        templates += json.dumps(generate_item_template(item_path.split("/")[-1]))
        templates += ","
    return templates


if __name__ == "__main__":
    item_paths = [
        "WorldExplorers/Content/Characters/Classes/MartialArtist/Multi_TripleCombo/CD_MartialArtist_SR2_Dark_TripleCombo_T06",
        "WorldExplorers/Content/Characters/Classes/Archer/Multi_PenetratingShot/CD_Archer_SR2_Dark_PenetratingShot_T06",
        "WorldExplorers/Content/Characters/Classes/Assassin/Multi_Doubletap/CD_Assassin_SR2_Dark_Doubletap_T06",
        "WorldExplorers/Content/Characters/Classes/Assassin/Multi_Doubletap/CD_Assassin_SR2_Fire_Doubletap_T06",
        "WorldExplorers/Content/Characters/Classes/Spellsword/Fire_ImbueFire/CD_Spellsword_SR2_Fire_ImbueFire_T06",
        "WorldExplorers/Content/Characters/Classes/Cleric/Multi_BurstHeal/CD_Cleric_R2_Light_BurstHeal_T06",
        "WorldExplorers/Content/Characters/Classes/Warmage/Multi_Starblast/CD_Warmage_VR2_Light_StarBlast_T06",
        "WorldExplorers/Content/Characters/Classes/MartialArtist/Multi_TripleCombo/CD_MartialArtist_SR2_Light_TripleCombo_T06",
        "WorldExplorers/Content/Characters/Classes/Assassin/Multi_Doubletap/CD_Assassin_SR2_Light_Doubletap_T06",
        "WorldExplorers/Content/Characters/Classes/Cleric/Multi_BurstHeal/CD_Cleric_R2_Nature_BurstHeal_T06",
        "WorldExplorers/Content/Characters/Classes/Assassin/Multi_Doubletap/CD_Assassin_SR2_Nature_Doubletap_T06",
        "WorldExplorers/Content/Characters/Classes/Cleric/Multi_BurstHeal/CD_Cleric_R2_Water_BurstHeal_T06",
        "WorldExplorers/Content/Characters/Classes/Assassin/Multi_Doubletap/CD_Assassin_SR2_Water_Doubletap_T06"
    ]
    print(generate_item_templates(item_paths))
