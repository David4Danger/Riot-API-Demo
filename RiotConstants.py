URL = {'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
       'summoner_by_name': 'v{version}/summoner/by-name/{names}',
       'stats_by_summoner_summary': 'v{version}/stats/by-summoner/{summonerId}/summary'}
#The first line is the 'base' part of the request url, used in every request.
#The following lines are all the extended part of the url, that is unique to each request.

API_VERSIONS = {'summoner': '1.4',
                'stats': '1.3'}
#These are the latest versionsof each type of request we'll use

REGIONS = {'europe_west': 'euw',
           'north_america': 'na',
           'korea': 'kr'}
#These are the regions and their appropriate acronyms that we can use to obtain information
#from, I usually use 'north_america', there is about 10 different regions you can use here.