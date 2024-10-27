# wiki-gen-poc

This serves as a proof of concept of a page generator for BTA wiki. Ideally this should run quickly enough so as to be able to run from a Github Action.

# How it works

## Iteration 5
Basically works like Iteration 4 except now 

1. The scripts can call each other as necessary
2. Instead of writing out a given wikitable to a file, it posts it to the wiki as a template
3. Credentials for that posting exist as env vars only - this is for Github Action integration

## Next Steps

1. Do up the redirects for all the broken links (look into jinja conditionals to maybe do this automatically for big win items like FCS, heat sinks, etc)
2. Reformat into Github Actions friendly format, post to BTA Org
3. Github Actions demo
4. Optimizations to keep Actions time as low as possible (hello async clients my old friends)

### Out of Scope

1. I think there's a way to get the weapon data into semi-useful tables in an automated fashion what's dumped in by the exporter via Lua modules, but I expect we'd need to drop columns, so more stuff for BD to approve. 
2. ~~server updates to allow stuff like this to run on the scale of the List of Mechs without blowing up~~ Works fine for Faction Stores! 🎉

<details>
<summary>Iteration 4</summary>
1. `factionParser` takes two arguments currently: a source directory to walk through and a prefix exception (`itemCollection_` in this case. This was part of the generifying bits but it may be dropped for ease of executioni/legibility down the line). 
2. It then recursively walks that directory for .json files and grabs the `items` entry. 
3. It then builds an index of all the .csv files in the source directory, again recursively to catch the fucking `StreamingAssets` split and uses the `items` entry to find the right Collection with and starts adding everything to a list with the `add_file_contents` function.
4. If `add_file_contents` finds something that starts with the `prefix` it *recursively calls itself* until it's built a clean list and kicks everything back up the chain.
5. `factionParser` then returns a dict of dicts that has all the information we care about, i.e. shit like "Weapon_Gauss_Light_0-STOCK". This obviously isn't useful for the wiki. Enter `factionRenderer`. 
6. `<handwavium>` Imagine `factionRenderer` is set up to pull a dict of dicts from factionParser `</handwavium>`. I'll deal with this later along with the POST of the data to the wiki. At the moment everything just writes out files and I wanted to get clearance to proceed before doing any HTTP crap that requires credentials.
7. `factionRenderer` searches for the .json that the entry "Weapon_Gauss_Light_0-STOCK" refers to. Within that, it grabs Description.UIName and does some light transformations. Emphasis on *light* because we are pursuing a goal of "good enough"
8. Then it uses my old enemy jinja to template out the wikitext we want. This is where more "good enough" comes in. I am proposing we don't try to send people to the specific subsection of, say, [Weapons](https://www.bta3062.com/index.php?title=Weapons), which frequently *has no syntactic relation to the fucking name of the weapon*, which is exacerbated by the fact that there's no fucking way to definitively tell what kind of weapon a something is from its json. Instead, users get sent to [Weapons](https://www.bta3062.com/index.php?title=Weapons) and can CTRL+F the rest of the way like adults. 
9. `<handwavium>` Imagine things get POSTed`</handwavium>` to the wiki as Templates, like [so](https://www.bta3062.com/index.php?title=Template:RasalhagueStore). This can then be called within its own page, via a [nested template](https://www.bta3062.com/index.php?title=Faction_Store_Example&action=edit) (i.e. `{{FStoreWrapper|{{RasalhagueStore}}}}`), or on the Faction Stores page alongside any number of others (i.e. {{FStoreWrapper|{{RasalhagueStore}}{{DavionStore}}{{etcStore}}}}`). 
10. This way, changes are sectioned off away from the main body of the text, and edits are easier to make. The downside is that this requires more manual intervention to set things up. The upside is fewer 10,000 character writes as the whole page is rewritten on every update again, a more easily approachable editing experience for minions and clear and legibile code in the most popular language on the planet that rank amateurs can update and manipulate.
11. Pieces that aren't easily caught by this automation (for a variety of reasons, some listed in rants above) would be manually updated with a redirect. e.g. the FCS attachments would get a redirect to the Attachments page.
</details>

<details>
<summary>Iteration 3</summary>
python3 factionParser.py ~/fungit/BattleTech-Advanced/DynamicShops/fshops
build this out
</details>

<details>
<summary>Iteration 2</summary>
1. Template for a whole table (with escaped `{{}}`!) is in `templates/factionStore.tpl`
2. That is rendered out with information hardcoded in `factionRenderer.py`
3. Ends up in `factionTable.wiki`
4. Example: https://www.bta3062.com/index.php?title=User:Amidatelion



<details>
<summary>Iteration 1</summary>

1. Template for just the table internals is in `factionStore.tpl`  
2. That is rendered out with information hardcoded in `factionRenderer.py`  
3. Ends up in `factionTable.wiki`  
<details>