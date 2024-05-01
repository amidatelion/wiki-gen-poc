# wiki-gen-poc

This serves as a proof of concept of a page generator for BTA wiki. Ideally this should run quickly enough so as to be able to run from a Github Action.

# How it works

# Iteration 2
1. Template for a whole table (with escaped `{{}}`!) is in `templates/factionStore.tpl`
2. That is rendered out with information hardcoded in `factionRenderer.py`
3. Ends up in `factionTable.wiki`
4. Example: https://www.bta3062.com/index.php?title=User:Amidatelion

# Next Steps

1. Remove hardcoding.
2. Figure out how to store item names with links (i.e. how to map `Weapon_Autocannon_UAC10_0-STOCK` to `[[Weapons#Ultra Autocannons|UAC/10]]`) (the answer, unfortunately, is probably SQLite)
3. From there, generate context on the fly
4. ???
5. Profit

<details>
<summary>Iteration 1</summary>

1. Template for just the table internals is in `factionStore.tpl`  
2. That is rendered out with information hardcoded in `factionRenderer.py`  
3. Ends up in `factionTable.wiki`  
<details>