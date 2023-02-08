from sanic import Sanic
import sanic
import asyncio
import json
import requests
import os
import shutil
import aiohttp
app = Sanic("backend")
ini = "ini"



@app.route('/fortnite/api/cloudstorage/system')
async def test(request):
    return sanic.response.json(json.load(open("json/cloudstorage.json")))

@app.route('/fortnite/api/cloudstorage/system/<file>')
async def test(request, file: str):
  if file != "config":
    return sanic.response.raw(open("ini/" + file).read())
  else:
    return sanic.response.json('')

@app.route('/content/api/pages/fortnite-game')
async def test(request):
    r = json.load(open("json/fngame.json"))
    return sanic.response.json(r)

@app.route('/content/api/pages')
async def test(request):
    r = json.load(open("json/fngame.json"))
    return sanic.response.json(r)
  
@app.route('/fortnite/api/storefront/v2/catalog')
async def test(request):
    r = json.load(open("json/shop.json"))
    return sanic.response.json(r)

@app.route('/api/v1/fortnite-br/surfaces/motd/target', methods=['GET', 'POST'])
async def test(request):
    r = json.load(open("json/motd.json"))
    return sanic.response.json(r)

async def LoadSettings(accountid, mode):
  settings = open(f"Account/{accountid}/Config.json")
  athena = open("Def/athena.json")
  pchanges = open(f"Account/{accountid}/profileChanges.json")
  if mode == "athena":
    f = json.load(athena)
    r = json.load(settings)
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["Character"]["items"][0] = r["Character0"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["Backpack"]["items"][0] = r["Backpack0"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["SkyDiveContrail"]["items"][0] = r["Contrail0"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["Dance"]["items"][0] = r["Emote0"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["Dance"]["items"][1] = r["Emote1"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["Dance"]["items"][2] = r["Emote2"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["Dance"]["items"][3] = r["Emote3"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["Dance"]["items"][4] = r["Emote4"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["Dance"]["items"][5] = r["Emote5"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["Glider"]["items"][0] = r["Glider0"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["LoadingScreen"]["items"][0] = r["LoadingScreen0"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["MusicPack"]["items"][0] = r["MusicPack0"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["ItemWrap"]["items"][0] = r["Wrap0"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["ItemWrap"]["items"][1] = r["Wrap1"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["ItemWrap"]["items"][2] = r["Wrap2"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["ItemWrap"]["items"][3] = r["Wrap3"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["ItemWrap"]["items"][4] = r["Wrap4"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["ItemWrap"]["items"][5] = r["Wrap5"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["ItemWrap"]["items"][6] = r["Wrap6"]
    f["profileChanges"][0]["profile"]["items"]["loadout1"]["attributes"]["locker_slots_data"]["slots"]["Pickaxe"]["items"][0] = r["Pickaxe0"]
    f["profileChanges"][0]["profile"]["stats"]["attributes"]["level"] = r["Level"]
    f["profileChanges"][0]["profile"]["stats"]["attributes"]["battlestars"] = r["BattleStars"]
    f["profileChanges"][0]["profile"]["stats"]["attributes"]["xp"] = r["Xp"]
    f["profileChanges"][0]["profile"]["stats"]["attributes"]["xp"] = r["Xp"]
    f["profileChanges"][0]["profile"]["items"]["VictoryCrown_defaultvictorycrown"]["total_royal_royales_achieved_count"] = r["Crowns"]
    f['profileChanges'][0]['profile']['items']["loadout1"]['attributes']['locker_slots_data']['slots']['Character']['activeVariants'][0]['variants'] = r['Character_Variants']
    f['profileChanges'][0]['profile']['items']["loadout1"]['attributes']['locker_slots_data']['slots']['Backpack']['activeVariants'][0]['variants'] = r['Backpack_Variants']
    if r["Removed_Items"] == []: 
      return f
    else:
       for i in r["Removed_Items"]:
         del f['profileChanges'][0]['profile']['items'][i]
    return f
  if mode == "pchanges":
    f = json.load(pchanges)
    r = json.load(settings)
    f["profileChanges"][0]["attributeValue"]["slots"]["Character"]["items"][0] = r["Character0"]
    f["profileChanges"][0]["attributeValue"]["slots"]["Backpack"]["items"][0] = r["Backpack0"]
    f["profileChanges"][0]["attributeValue"]["slots"]["Pickaxe"]["items"][0] = r["Pickaxe0"]
    f["profileChanges"][0]["attributeValue"]["slots"]["SkyDiveContrail"]["items"][0] = r["Contrail0"]
    f["profileChanges"][0]["attributeValue"]["slots"]["Dance"]["items"][0] = r["Emote0"]
    f["profileChanges"][0]["attributeValue"]["slots"]["Dance"]["items"][1] = r["Emote1"]
    f["profileChanges"][0]["attributeValue"]["slots"]["Dance"]["items"][2] = r["Emote2"]
    f["profileChanges"][0]["attributeValue"]["slots"]["Dance"]["items"][3] = r["Emote3"]
    f["profileChanges"][0]["attributeValue"]["slots"]["Dance"]["items"][4] = r["Emote4"]
    f["profileChanges"][0]["attributeValue"]["slots"]["Dance"]["items"][5] = r["Emote5"]
    f["profileChanges"][0]["attributeValue"]["slots"]["ItemWrap"]["items"][0] = r["Wrap0"]
    f["profileChanges"][0]["attributeValue"]["slots"]["ItemWrap"]["items"][1] = r["Wrap1"]
    f["profileChanges"][0]["attributeValue"]["slots"]["ItemWrap"]["items"][2] = r["Wrap2"]
    f["profileChanges"][0]["attributeValue"]["slots"]["ItemWrap"]["items"][3] = r["Wrap3"]
    f["profileChanges"][0]["attributeValue"]["slots"]["ItemWrap"]["items"][4] = r["Wrap4"]
    f["profileChanges"][0]["attributeValue"]["slots"]["ItemWrap"]["items"][5] = r["Wrap5"]
    f["profileChanges"][0]["attributeValue"]["slots"]["ItemWrap"]["items"][6] = r["Wrap6"]
    f["profileChanges"][0]["attributeValue"]["slots"]["MusicPack"]["items"][0] = r["MusicPack0"]
    f["profileChanges"][0]["attributeValue"]["slots"]["Glider"]["items"][0] = r["Glider0"]
    f["profileChanges"][0]["attributeValue"]["slots"]["LoadingScreen"]["items"][0] = r["LoadingScreen0"]
    f['profileChanges'][0]['attributeValue']['slots']["Character"]['activeVariants'][0]['variants'] = r['Character_Variants']
    f['profileChanges'][0]['attributeValue']['slots']["Backpack"]['activeVariants'][0]['variants'] = r['Backpack_Variants']
    
    return f
  if mode == "common_core":
    f = json.load(open("Account/" + accountid + "/common_core.json"))
    r = json.load(settings)
    f["profileChanges"][0]["profile"]["items"]["Currency"]["quantity"] = r["Vbucks"]
    return f
    
  return


async def CheckValidFortId(id):
  async with aiohttp.request('GET', 'https://fortnite-api.com/v2/stats/br/v2/' +id, headers = {'Content-Type': 'application/json',
                'Authorization': '57c14674-da4d-4afe-b0e3-6bef6edbc751' }) as r:
  
    if r.status == 200 or r.status == 403:
         return True
  return False       
  
def RefreshCosmetics():
  r = requests.get("https://fortnite-api.com/v2/cosmetics/br/new").json()['data']['items']
  athena = open('Def/athena.json')
  x = json.load(athena)
  for i in r:
      variants = []
      owned = []
      if i['variants'] != None:
           for u in i['variants'][0]['options']:
             owned.append(u['tag'])
           for c in i['variants']:
            variants.append({
                    "channel": c['channel'],
                    "active": c['options'][0]['tag'],
                    "owned": owned
                })
      dict = {
        i['type']['backendValue'] + ":" + i['id']: {
                  "templateId": i['type']['backendValue'] + ":" + i['id'],
                  "attributes":{
                     "max_level_bonus":0,
                     "level":1,
                     "item_seen":True,
                     "xp":0,
                     "variants":variants,
                     "favorite":False
                  },
                  "quantity":1
               }
        }
      
      f = x['profileChanges'][0]['profile']['items'].get(i['type']['backendValue'] + ":" + i['id'])
      if f == None:
        x['profileChanges'][0]['profile']['items'].update(dict)
        n = open('Def/athena.json', 'w')
        json.dump(x, n, indent=3)
        n.close()
        print ("Added - " + i['type']['backendValue'] + ":" + i['id'])
  print('Reloaded Cosmetics!')
  return

async def RefreshCosmeticsAsync():
  r = requests.get("https://fortnite-api.com/v2/cosmetics/br/new").json()['data']['items']
  athena = open('Def/athena.json')
  x = json.load(athena)
  for i in r:
      variants = []
      owned = []
      if i['variants'] != None:
           for u in i['variants'][0]['options']:
             owned.append(u['tag'])
           for c in i['variants']:
            variants.append({
                    "channel": c['channel'],
                    "active": c['options'][0]['tag'],
                    "owned": owned
                })
      dict = {
        i['type']['backendValue'] + ":" + i['id']: {
                  "templateId": i['type']['backendValue'] + ":" + i['id'],
                  "attributes":{
                     "max_level_bonus":0,
                     "level":1,
                     "item_seen":True,
                     "xp":0,
                     "variants":variants,
                     "favorite":False
                  },
                  "quantity":1
               }
        }
      
      f = x['profileChanges'][0]['profile']['items'].get(i['type']['backendValue'] + ":" + i['id'])
      if f == None:
        x['profileChanges'][0]['profile']['items'].update(dict)
        n = open('Def/athena.json', 'w')
        json.dump(x, n, indent=3)
        n.close()
        print ("Added - " + i['type']['backendValue'] + ":" + i['id'])
  print('Reloaded Cosmetics!')
  return

def RefreshCosmeticsBackup():
  r = requests.get("https://fortniteapi.io/v2/items/list?lang=en", headers={"Authorization": "b0b1a11e-dcafb389-48781fab-eda1aeb7"}).json()['items']
  athena = open('Def/athena.json')
  x = json.load(athena)
  for i in r:
      title = ''
      match i['type']['id']:
        case 'outfit':
          title = 'AthenaCharacter:' + i['id']
        case 'emote':
          title = 'AthenaDance:' + i['id']
        case 'backpack':
          title = 'AthenaBackpack:' + i['id']
        case 'pickaxe':
          title = 'AthenaPickaxe:' + i['id']
        case 'glider':
          title = 'AthenaGlider:' + i['id']
        case 'contrail':
          title = 'AthenaSkyDiveContrail:' + i['id']
        case 'music':
          title = 'AthenaMusicPack:' + i['id']
        case 'wrap':
          title = 'AthenaItemWrap:' + i['id']
        case 'loadingscreen':
          title = 'AthenaLoadingScreen:' + i['id']
      
     
      variants = []
      dict = {
        title: {
                  "templateId": title,
                  "attributes":{
                     "max_level_bonus":0,
                     "level":1,
                     "item_seen":True,
                     "xp":0,
                     "variants":variants,
                     "favorite":False
                  },
                  "quantity":1
               }
        }
      
      if x['profileChanges'][0]['profile']['items'].get(title) == None:
         print("Added - " + title)
         x['profileChanges'][0]['profile']['items'].update(dict)
         n = open('Def/athena.json', 'w')
         json.dump(x, n, indent=3)
         n.close()
  print('Reloaded Cosmetics!')
  return
    



@app.route('/fortnite/api/game/v2/profile/<accountId>/client/<command>', methods=["GET", "POST"])
async def test(request, accountId: str, command: str):
    if os.path.exists("Account/" + accountId) == False and await CheckValidFortId(accountId) == True:
      os.makedirs("Account/" + accountId)
      for i in os.listdir("Def"):
        shutil.copyfile(f"Def/{i}", f"Account/{accountId}/{i}")
    if command == "SetCosmeticLockerSlot":
      pchanges = json.load(open("Account/" + accountId + "/profileChanges.json"))
      #pfile = open("Account/" + accountId + "/profileChanges.json", 'r+')
      settings = open("Account/" + accountId + "/Config.json", "r+")
      ConfigFile = "Account/" + accountId + "/Config.json"
      f = json.load(open("Account/" + accountId + "/athena.json", 'r+'))
      #ff = open("Account/" + accountId + "/athena.json" ,'r+')
      body = json.loads(request.body)["category"]
      slot = json.loads(request.body)["itemToSlot"]
      
      if "slotIndex" in json.loads(request.body):
         slotIndex = json.loads(request.body)["slotIndex"]
      else:
         slotIndex = 0
      jsettings = json.load(settings)
      if body + "_Variants" in jsettings:
        jsettings[body + "_Variants"] = json.loads(request.body)['variantUpdates']
      if "Dance" in body:
        body = "Emote"
      if "SkyDiveContrail" in body:
        body = "Contrail"
      if str(slotIndex) == "-1":
        for k in jsettings:
          if "Wrap" in k:
           
              jsettings[k] = slot 

              dict = jsettings
              f = open(ConfigFile, 'w+')
              f.write(json.dumps(dict))
              f.close()
              return sanic.response.json(await LoadSettings(accountId, "pchanges"))
        

      jsettings[body + str(slotIndex)] = slot
      
      dict = jsettings
      f = open(ConfigFile, 'w+')
      f.write(json.dumps(dict))
      f.close()
      
            
      return sanic.response.json(await LoadSettings(accountId, "pchanges"))
    elif command == "QueryProfile":
        body = request.args["profileId"][0]
        if body == "athena":
          return sanic.response.json(await LoadSettings(accountId, "athena"))
        elif body == "common_core":
          return sanic.response.json(await LoadSettings(accountId, "common_core"))
          print(body)
        else:
          f = json.load(open("Account/" + accountId + f"/{body}.json"))
          return sanic.response.json(f)
    elif command == "ClientQuestLogin":
       return sanic.response.json(json.loads('{"profileRevision":6969,"profileId":"athena","profileChangesBaseRevision":6969,"profileChanges":[],"serverTime":"2023-01-29T19:04:47.462Z","profileCommandRevision":4200,"responseVersion":1}'))
    elif command == "SetMtxPlatform":
      return sanic.response.json(await LoadSettings(accountId, "common_core"))
    elif command == "RemoveGiftBox":
      commoncore = open("Account/" + accountId + "/common_core.json")
      cc = json.load(commoncore)
      del(cc["profileChanges"][0]['profile']["items"]['gifting'])
      return sanic.response.json(cc)
    else:
      return sanic.response.json(json.load(open("Account/" + accountId + "/" + request.args["profileId"][0] + ".json")))
   
@app.route('/stats/<stat>/<amount>/<accountid>')
async def test(request, stat: str, accountid: str, amount: int):
    f = json.load(open('Account/' + accountid + "/Config.json"))
    if stat == 'battlestars':
      f['BattleStars'] = amount
    else:
      f[stat.capitalize()] = amount
    g = open ('Account/' + accountid + "/Config.json", 'w')
    g.write(json.dumps(f))
    return sanic.response.json(f)

@app.route('/locker/<action>/<id>/<accountid>')
async def test(request, action: str, accountid: str, id: str):
    f = json.load(open('Account/' + accountid + "/Config.json"))
    if action == 'remove':
      f['Removed_Items'].append(id)
    elif action == "add":
      try:
        f["Removed_Items"].remove(id)
      except: pass
    elif action == "clear":
      f["Removed_Items"] = "all"
    elif action == "reset":
      f["Removed_Items"] = []
    g = open ('Account/' + accountid + "/Config.json", 'w')
    g.write(json.dumps(f))
    return sanic.response.json(f)


Gifting = {
      
      "templateId": "GiftBox:GB_Default",
      "attributes": {
        "max_level_bonus": 0,
        "fromAccountId": "",
        "lootList": [
          {
            "itemType": "ItemId",
            "itemGuid": "ItemId",
            "itemProfile": "ItemProfile",
            "quantity": 1
          } 
        ]
      }
    }

@app.route("/refreshcosmetics")
async def test(request):
  await RefreshCosmeticsAsync()
  return sanic.response.json("lol", "Refreshed Cosmetics!")


@app.route('/gifting/seperate/<id>/<giftbox>/<accountid>')
async def test(request, id: str, accountid: str, giftbox: str):
    f = Gifting
    f['templateId'] = "AthenaGiftBox:" + giftbox
    f['attributes']['lootList'][0]['itemType'] = id
    f['attributes']['lootList'][0]['itemGuid'] = id
    f['attributes']['lootList'][0]['itemProfile'] = 'athena'
    r = open ('Account/' + accountid + "/common_core.json")
    x = json.load(r)
    x['profileChanges'][0]['profile']['items']['gifting'] = f
    g = open('Account/' + accountid + "/common_core.json", 'w')
    g.write(json.dumps(x))
    return sanic.response.json(x)

@app.route('/gifting/vbucks/<amount>/<giftbox>/<accountid>')
async def test(request, amount: str, accountid: str, giftbox: str):
    f = Gifting
    f['gifting']['templateId'] = "AthenaGiftBox:" + giftbox
    f['gifting']['attributes']['lootList'][0]['itemType'] = "Currency:MtxPurchased"
    f['gifting']['attributes']['lootList'][0]['itemGuid'] = "Currency:MtxPurchased"
    f['attributes']['lootList'][0]['itemProfile'] = 'common_core'
    f['attributes']['lootList'][0]['quantity'] = int(amount)
    r = open ('Account/' + accountid + "/common_core.json")
    x = json.load(r)
    x['profileChanges'][0]['profile']['items']['gifting'] = f
    g = open('Account/' + accountid + "/common_core.json", 'w')
    g.write(json.dumps(x))
    return sanic.response.json(x)

@app.route('/gifting/all/<accountid>/<giftbox>/<type>')
async def test(request, amount: str, accountid: str, type: str, giftbox: str):
    f = Gifting
    h = json.loads(open('Def/athena.json'))['profileChanges'][0]['profile']['items']
    bh = 0 
    for i in h:
      if type in i:
        f['gifting']['templateId'] = "AthenaGiftBox:" + giftbox
        f['gifting']['attributes']['lootList'][bh]['itemType'] = i
        f['gifting']['attributes']['lootList'][bh]['itemGuid'] = i
        f['gifting']['attributes']['lootList'][bh]['itemProfile'] = 'common_core'
        f['gifting']['attributes']['lootList'][bh]['quantity'] = int(amount)
        bh += 1
    r = open ('Account/' + accountid + "/common_core.json")
    x = json.load(r)
    x['profileChanges'][0]['profile']['items']['gifting'] = f
    g = open('Account/' + accountid + "/common_core.json", 'w')
    g.write(json.dumps(x))
    return sanic.response.json(x)
    

@app.route('/')
async def test(request):
    o = 0
    for i in os.listdir('Account'):
      o += 1
    return sanic.response.text("atomicv4 has " + str(o) + " users!")


RefreshCosmetics()


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, access_log=True)
  

  