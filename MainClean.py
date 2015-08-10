from RiotAPI import RiotAPI
def main():
        api = RiotAPI('YOUR API KEY HERE!')
        res = api.get_summoner_by_name('streetjustlce')
        ID = (res['streetjustlce']['id'])
        
        res2 = api.stats_by_summoner_summary(ID)
        print((res2['playerStatSummaries'][-2]["wins"]) / (res2['playerStatSummaries'][-2]["losses"])) 
    
if __name__ == "__main__":
        main()