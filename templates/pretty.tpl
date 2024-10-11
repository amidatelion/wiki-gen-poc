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
! [[File:{faction_info.logo}}|link={{faction_info.link}}|75px]] 
[[{{faction_info.link|{{faction_info.name}}]]
| {% for weapon in weapons %}
[[ {{weapon}} ]]</br>
{% endfor %}
| {% for ammunition in ammunitions %}
[[ {{ ammunition }}]]
{% endfor %}
| {% for gear in gears %}
[[{{ gear }}]]
{% endfor %}
| {% for mech in mechs %}
[[{{ mech }}]]
{% endfor %}
| {% for mechpart in mechparts %}
[[{{ mechpart }}]]
{% endfor %}
| {% for vehicle in vehicles %}
[[{{ vehicle }}]]
{% endfor %}
| {% for battlearmor in battlearmors %}
[[{{ battlearmor }}]]
{% endfor %}
| {% for contract in contracts %}
[[{{ contract }}]]
{% endfor %}