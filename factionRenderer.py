from jinja2 import Environment, FileSystemLoader


environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("pretty.tpl")

example_dict =  {'Rasalhague.json': ['Weapon_Autocannon_LB10XAC',
                     'Weapon_PPC_PPC_SNUBNOSE',
                     'Weapon_Autocannon_UAC5_0-STOCK',
                     'Weapon_SRM_SSRM2_0-STOCK',
                     'Ammo_AmmunitionBox_LBX_CLUSTER_AC10',
                     'Ammo_AmmunitionBox_LBX_SLUG_AC10',
                     'Ammo_AmmunitionBox_Ultra_AC5',
                     'Ammo_AmmunitionBox_Streak_SRM',
                     'mechdef_viking_VKG-2F',
                     'mechdef_vonrohrs_VON-4RH-5',
                     'mechdef_vonrohrs_VON-4RH-6',
                     'vehicledef_REDKITE',
                     'vehicledef_UNNSVIN',
                     'vehicledef_UNNSVIN_BALLISTIC',
                     'vehicledef_UNNSVIN_MISSILE',
                     'vehicledef_TAGDRONE',
                     'vehicledef_VTOLDRONE',
                     'mechdef_ba_krupp',
                     'Weapon_Medium_Recoilless_BA',
                     'Gear_Attachment_AutocannonFCS',
                     'Gear_Attachment_PPCFCS',
                     'Gear_Contract_Mech_Gunslinger_FRR',
                     'Gear_Contract_BattleArmor_Krupp_Rasalhague']}

codebase_dir = "/home/eadderley/fungit/BattleTech-Advanced"

def render_factionstore(faction, items):
    faction_name = faction[:-5]
    results_filename = faction_name+"_store_Table.wiki"
    faction_info=get_faction_specific_info(faction_name)
    weapons = []
    ammunitions = []
    gears = []
    mechs = []
    mechparts = []
    vehicles = []
    battlearmors = []
    contracts = []
    for item in items:
        if item.startswith("Weapon_"):
            weapons.append(item)
        elif item.startswith("Ammo_"):
            ammunitions.append(item)
        elif item.startswith("Gear_", "emod_")and not item.startswith("Gear_Contract_"):
            gears.append(item)
        elif item.startswith("mechdef_") and not item.startswith("mechdef_ba"):
            mechs.append(item)
        elif item.startswith("mechpartdef_"):
            mechparts.append(item)
        elif item.startswith("vehicledef_"):
            vehicles.append(item)
        elif item.startswith("mechdef_ba"):
            battlearmors.append(item)
        elif item.startswith("Gear_Contract_"):
            contracts.append(item)
    
    for index, item in enumerate(weapons):
        weapons[index] = get_display_name(item)
    for index, item in enumerate(ammunitions):
        ammunitions[index] = get_display_name(item)
    for index, item in enumerate(gears):
        gears[index] = get_display_name(item)
    for index, item in enumerate(mechs):
        mechs[index] = get_display_name(item)
    for index, item in enumerate(mechparts):
        mechparts[index] = get_display_name(item)
    for index, item in enumerate(vehicles):
        vehicles[index] = get_display_name(item)
    for index, item in enumerate(battlearmors):
        battlearmors[index] = get_display_name(item)
    for index, item in enumerate(contracts):
        contracts[index] = get_display_name(item)

    context = {
    "faction_info": faction_info,
    "weapons": weapons,
    "ammunitions": ammunitions,
    "gears": gears,
    "mechs": mechs,
    "mechparts": mechparts,
    "vehicles": vehicles, 
    "battlearmors": battlearmors,
    "contracts": contracts,
    }

    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"... wrote {results_filename}")


def get_faction_specific_info(faction):
    faction_lookup = {"Rasalhague": {"logo":"Cameron_logo.png", "name":"Terran Hegemony (Cameron)", "link":"Terran Hegemony"}},
    return faction_lo          okup[faction]

def get_display_name(item):
    for root, dirs, files in os.walk(codebase_dir):
        for file in files:
            # Check if the file is the target JSON file
            if file == item+".json":
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    # Check if 'Description' and 'UIName' exist
                    ui_name = data['Description']['UIName']
                    return ui_name


if __name__ == "__main__":
    for faction,items in example_dict.items():
        render_factionstore(faction, items)
        
