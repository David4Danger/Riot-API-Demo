import requests #make sure you've installed this!
import RiotConstants as RC #this is the last file we made

class RiotAPI(object):
    
    def __init__(self, api_key, region=RC.REGIONS['north_america']): #can change this to any region
        self.api_key = api_key
        self.region = region
    
    def _request(self, api_url, params={}): #our request function
        entries = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in entries:
                entries[key] = value
        
        reply = requests.get(
            RC.URL['base'].format( #we are formatting the 'base' string from RC
                proxy = self.region,
                region = self.region,
                url = api_url),
            params = entries)
        
        return reply.json() #this is the information our request to Riot API gives back to us!
    
    def get_summoner_by_name(self, sumname): #this function takes summoner name, returns lots of info (ID!)
        api_url = RC.URL['summoner_by_name'].format(
            version = RC.API_VERSIONS['summoner'],
            names = sumname)
        return self._request(api_url)
    
    def stats_by_summoner_summary(self, sumid): #this function takes summoner ID, returns stat summary
        api_url = RC.URL['stats_by_summoner_summary'].format(
            version = RC.API_VERSIONS['stats'],
            summonerId = sumid)
        return self._request(api_url)