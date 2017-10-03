import apiMethods as api

#the api_key needed to access Riot API
KEY = "RGAPI-877c39e4-d910-4fa0-a2fc-01d3090edea3"

region = "NA"
summName = "mostafa elsokari"

#summoner id of the given summoner name
summID = str(api.getSummData(region, summName, KEY)["id"])

#json containing the ranked info of the summoner name
rankedInfo = api.getRankedData(region, summID, KEY)

#extracting the necessary stats 
tier   = rankedInfo[0]["tier"]
rank   = rankedInfo[0]["rank"]
lp     = str(rankedInfo[0]["leaguePoints"])
wins   = str(rankedInfo[0]["wins"])
losses = str(rankedInfo[0]["losses"])

#printing the ranked stats extracted above
print("Summoner Name :   " + summName)
print(tier + "\n" + rank + "\n" + lp)
print("Wins :   " + wins + "\t" + "Losses :   " + losses)