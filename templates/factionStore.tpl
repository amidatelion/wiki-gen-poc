==Faction Store Inventory==
The Federated Suns faction store can be accessed in any of their systems after allying with them. [[Faction Stores|A list of all faction stores can be found here.]]

'''Legend:'''
*{% raw %}{{Highlight|Faction Unique|LightBlue}}{% endraw %}

{| class="wikitable " style="text-align: center"
! Faction
! Weapons
! Ammunition
! Equipment
! Full 'Mechs
! 'Mech Parts
! Vehicles
! Battle Armor
! Contracts
|-
! [[File:Davion_logo.png|link=Federated Suns|75px]] 
[[Federated Suns|Federated Suns (Davion)]]
| {% for weapon in weapons %}{{ weapon.item }}{% endfor %}
| {% for ammunition in ammunitions %}{{ ammunition.item }}{% endfor %}
| {% for gear in gears %}{{ gear.item }}{% endfor %}
| {% for mech in mechs %}{{ mech.item }}{% endfor %}
| {% for mechpart in mechparts %}{{ mechpart.item }}{% endfor %}
| {% for vehicle in vehicles %}{{ vehicle.item }}{% endfor %}
| {% for battlearmor in battlearmors %}{{ battlearmor.item }}{% endfor %}
| {% for contract in contracts %}{{ contracts.item }}{% endfor %}
|-
|}

