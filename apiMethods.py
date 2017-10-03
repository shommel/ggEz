import requests

#used to obtain summoner id needed for the ranked info lookup
def getSummData(region, summName, APIkey):
    
    #creating the url needed to access ranked stats
    #uses region, summoner name, and api key
     url = "https://" + region + "1.api.riotgames.com/lol/summoner/"\
     + "v3/summoners/by-name/" + summName + "?api_key=" + APIkey
     
     response = requests.get(url)
     
     return response.json()
 
def getRankedData(region, summID, APIkey):
    
    #creating the url needed to access ranked stats
    #uses region, summoner id, and api key
    url = "https://" + region + "1.api.riotgames.com/lol/league/"\
    + "v3/positions/by-summoner/" + summID + "?api_key=" + APIkey
    response = requests.get(url)
    
    #returning the json dict from riot api
    return response.json()

