from RiotAPI import RiotAPI
def main():
        api = RiotAPI('a14bbd5a-586a-469d-97dd-9beddfd95e2b') #my old key
        res = api.get_summoner_by_name('streetjustlce') #result of summoner by name func
        print (type(res)) #should be a dictionary
        print(res) #is the summoner info dictionary
        ID = (res['streetjustlce']['id']) #summoner id found from res
        print(ID) #actual
        
        res2 = api.stats_by_summoner_summary(ID) #result of the stats by summoner func, used ID found earlier!
        print(type(res2)) #should once again be a dictionary
        #print(res2) #this is a HUGE dictionary, much easier to see what is returned by looking at the Riot dev website!
        print((res2['playerStatSummaries'][-2]["wins"]) / (res2['playerStatSummaries'][-2]["losses"])) 
        #above is the ranked solo wins/ranked solo losses, found from stats by summoner id function!
    
if __name__ == "__main__": #so our file can act as a standalone program
        main()
