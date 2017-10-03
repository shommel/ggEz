import apiMethods as api
import tkinter as tk
import time

#the method needed to close the tk window  
def _quit():
    window.destroy()
    quit()

#function to easily create labels 
def createLabel(stat, info):
    label = tk.Label(window, text = stat + ":   " + info)
    label.pack()
    
#if the desired info cannot be found, produces error label
#waits 10 seconds, then closes the window and program
def errorHandel(info):
    labelError = tk.Label(window, text = "Error finding " + info + ". " + 
                          "Closing in 5 seconds.")
    labelError.pack()
    window.update()
    time.sleep(5)
    window.destroy()
    quit()

#the fuction called when the search button is clicked
def search():
    #the api_key needed to access Riot API
    KEY = "RGAPI-a8b7be4b-ca62-4572-8f55-08396223958e"
    
    #obtaining the region from the dropdown menu
    region = option.get()
    
    #obtaining the summoner name from the text field
    summName = summIn.get()
    
    #summoner ID loop
    try:
        #summoner id of the given summoner name
        summID = str(api.getSummData(region, summName, KEY)["id"])
    
    except:
        errorHandel("summoner name")
    
    #ranked stats loop
    try:
        #json containing the ranked info of the summoner name
        rankedInfo = api.getRankedData(region, summID, KEY)

        #extracting the necessary stats 
        tier   = rankedInfo[0]["tier"]
        rank   = rankedInfo[0]["rank"]
        lp     = str(rankedInfo[0]["leaguePoints"])
        wins   = str(rankedInfo[0]["wins"])
        losses = str(rankedInfo[0]["losses"])
        
    except:
        errorHandel("ranked stats")
        
    #destroying the previous buttons and text field
    region_menu.destroy()
    summIn.destroy()
    buttonSearch.destroy()
    
    #creating labels for each of the ranked stats above
    createLabel("Summoner Name", summName) 
    createLabel("Region", region)
    createLabel("Tier", tier)
    createLabel("Rank", rank)
    createLabel("LP", lp)
    createLabel("Wins", wins)
    createLabel("Losses", losses)

    #creating the quit button
    buttonClose = tk.Button(window, text = "Quit", command = _quit)
    buttonClose.pack()
       
#creating tkinter window
window = tk.Tk()
window.wm_title("Ranked Stats")

##creating a header for the window
#header = tk.Label(window, text="Ranked Stats", bg="black", fg="white")
#header.pack()

#creating a label with a pic the lol logo
logoRef = tk.PhotoImage(file="logo.gif")
logo = tk.Label(image=logoRef)
logo.pack()

#adding a dropdown menu of the regions
option = tk.StringVar(window)
option.set("NA")
region_menu = tk.OptionMenu(window, option, "NA", "EUW", "EUN", "BR", "JP")
region_menu.pack()

#text field where the summoner name will be input
summIn = tk.Entry(window)
summIn.pack()

#packing the search button
buttonSearch = tk.Button(window, text = "Search", command = search)
buttonSearch.pack()


tk.mainloop()