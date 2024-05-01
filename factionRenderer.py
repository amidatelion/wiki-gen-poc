from jinja2 import Environment, FileSystemLoader


weapons = [
    {"item": "[[Weapons#BA Light Recoilless Rifle|BA Light Recoilless Rifle]]</br>"},
    {"item": "[[Weapons#Single Shot|BA Magshot Gauss Rifle]]</br>"},
    {"item": "[[Weapons#BA Light Recoilless Rifle|BA Light Recoilless Rifle]]</br>"},
    {"item": "[[Weapons#Single Shot|BA Magshot Gauss Rifle]]</br>"},
    {"item": "[[Weapons#BA SMG|BA SMG]]</br>"},
    {"item": "[[Weapons#Bomb Bays|Cluster Bomb]]</br>"},
    {"item": "[[Weapons#Bomb Bays|HiEx Bomb]]</br>"},
    {"item": "[[Weapons#Bomb Bays|Inferno Bomb]]</br>"},
    {"item": "[[Weapons#Mech Taser|Mech Taser]]</br>"},
    {"item": "[[Weapons#Rotary Autocannons|Rotary AC/2]]</br>"},
    {"item": "[[Weapons#Rotary Autocannons|Rotary AC/5]]</br>"},
    {"item": "[[Weapons#Ultra Autocannons|UAC/2]]</br>"},
    {"item": "[[Weapons#Ultra Autocannons|UAC/5]]</br>"},
    {"item": "[[Weapons#Ultra Autocannons|UAC/10]]</br>"},
    {"item": "[[Weapons#Ultra Autocannons|UAC/20]]</br>"},
]
ammunitions = [
    {"item": "[[Ammunition#|Ammo LRM ARTIV]]</br>"},
    {"item": "[[Ammunition#|Ammo RAC/2]]</br>"},
    {"item": "[[Ammunition#|Ammo RAC/2 [Half]]]</br>"},
    {"item": "[[Ammunition#|Ammo RAC/5]]</br>"},
    {"item": "[[Ammunition#|Ammo RAC/5 [Half]]]</br>"},
    {"item": "[[Ammunition#|Ammo SRM ARTIV]]</br>"},
    {"item": "[[Ammunition#|Ammo Taser]]</br>"},
    {"item": "[[Ammunition#|Ammo UAC/2]]</br>"},
    {"item": "[[Ammunition#|Ammo UAC/5]]</br>"},
    {"item": "[[Ammunition#|Ammo UAC/10]]</br>"},
    {"item": "[[Ammunition#|Ammo UAC/20]]</br>"},
]
gears = [
    {"item": "[[Weapon_Attachments#Artemis IV FCS|Artemis IV FCS]]</br>"},
    {"item": "[[Weapon_Attachments#Autocannon FCS|Autocannon FCS]]</br>"},
    {"item": "[[Foot_Actuators#Foot Roundhouse + +|Foot Roundhouse + +]]</br>"},
    {"item": "[[Cooling#Heat Sink Freezer (D)|Heat Sink Freezer (D)]]</br>"},
    {"item": "[[Lower_Leg_Actuators#Lower Leg Muay Thai + +|Lower Leg Muay Thai + +]]</br>"},
    {"item": "[[Shoulder_Actuators#Shoulder Tackle + +|Shoulder Tackle + +]]</br>"},
    {"item": "{{Highlight|[[Armor#Ultra Ferro-Fibrous Armor|Ultra Ferro]]|LightBlue}}</br>"},
    {"item": "[[Upper_Arm_Actuators#Upper Arm Impede + +|Upper Arm Impede + +]]</br>"}
]
mechs = [
    {"item": "[[Argus#AGS-4D|Argus AGS-4D]]</br>"},
    {"item": "[[Battleaxe#BKX-8K|Battleaxe BKX-8K]]</br>"},
    {"item": "[[Bushwacker#BSW-X1|Bushwacker BSW-X1]]</br>"},
    {"item": "[[Chimera#CMA-1S|Chimera CMA-1S]]</br>"},
    {"item": "[[Dervish#DV-7D|Dervish DV-7D]]</br>"},
    {"item": "[[Enfield#END-6Q|Enfield END-6Q]]</br>"},
    {"item": "[[Enforcer II#ENF-5D|Enforcer II ENF-5D]]</br>"},
    {"item": "[[Fireball#ALM-8D|Fireball ALM-8D]]</br>"},
    {"item": "[[JagerMech II#JM7-F|JagerMech II JM7-F]]</br>"},
    {"item": "[[Osiris#OSR-3D|Osiris OSR-3D]]</br>"},
    {"item": "[[Penetrator#PTR-4D|Penetrator PTR-4D]]</br>"},
    {"item": "[[Salamander#PPR-5S|Salamander PPR-5S]]</br>"},
    {"item": "[[Griffin_(60T)#GRF-2N-X|Super Griffin GRF-2N-X]]</br>"},
    {"item": "[[Super Wasp#WSP-2A-X|Super Wasp WSP-2A-X]]</br>"},
    {"item": "[[Swordsman#SWD-3|Swordsman SWD-3]]</br>"},
    {"item": "[[Talon#TLN-5W|Talon TLN-5W]]</br>"},
    {"item": "[[Templar#TLR1-O|Templar TLR1-O]]</br>"},
    {"item": "[[Titan#TI-1A|Titan TI-1A]]</br>"},
    {"item": "[[Valkyrie II#VLK-II-2A|Valkyrie II VLK-II-2A]]</br>"},
    {"item": "[[Valkyrie#VLK-QD|Valkyrie VLK-QD]]</br>"},
    {"item": "[[Wasp LAM#WSP-103|Wasp LAM WSP-103]]</br>"}
]
mechparts = [
    {"item": "[[JagerMech II#JM7-D|JagerMech II JM7-D]]</br>"},
    {"item": "[[Valkyrie II#VLK-II-2A|Valkyrie II VLK-II-2A]]</br>"}
]
vehicles = [
    {"item": "[[Paladin#Paladin Prototype Defense System|Paladin Prototype Defense System]]</br>"},
]
mechparts = [
    {"item": "[[JagerMech II#JM7-D|JagerMech II JM7-D]]</br>"},
    {"item": "[[Valkyrie II#VLK-II-2A|Valkyrie II VLK-II-2A]]</br>"}
]
battlearmors = [
    {"item": "[[Grenadier Battle Armor#|Grenadier Battle Armor]]</br>"},
    {"item": "[[Infiltrator Mk II Battle Armor#|Infiltrator Mk II Battle Armor]]</br>"}
]
contracts = [
    {"item": "[[Contracts#Contract for Challenger Tank Airdrop|Contract for Challenger Tank Airdrop]]</br>"},
    {"item": "[[Contracts#Contract for Templar Airdrop|Contract for Templar Airdrop]]</br>"},
    {"item": "[[Contracts#Permanent Contract for Grenadier BA Airdrop|Permanent Contract for Grenadier BA Airdrop]]</br>"},
    {"item": "[[Contracts#Permanent Contract for Infiltrator Mk II BA Airdrop|Permanent Contract for Infiltrator Mk II BA Airdrop]]</br>"}
]
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("factionStore.tpl")

results_filename = "factionTable.wiki"
results_template = environment.get_template("factionStore.tpl")
context = {
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
