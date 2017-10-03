from apiMethods import getSummData

KEY = "RGAPI-f9cf3d8e-4e10-411c-9a6d-cbdd087c7100"

region = "NA"
summName = "mostafa elsokari"

#summoner id of the given summoner name
accID = str(getSummData(region, summName, KEY)["accountId"])

print(accID)
