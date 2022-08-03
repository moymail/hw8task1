import requests

intelligence_dict = {}

hulk_url = 'https://akabab.github.io/superhero-api/api/powerstats/332.json'
hulk_resp = requests.get(hulk_url)
hulk_dict = hulk_resp.json()
intelligence_dict['Hulk'] = hulk_dict['intelligence']

captain_america_url = 'https://akabab.github.io/superhero-api/api/powerstats/149.json'
captain_america_resp = requests.get(captain_america_url)
captain_america_dict = captain_america_resp.json()
intelligence_dict['Captain America'] = captain_america_dict['intelligence']

thanos_url = 'https://akabab.github.io/superhero-api/api/powerstats/655.json'
thanos_resp = requests.get(thanos_url)
thanos_dict = thanos_resp.json()
intelligence_dict['Thanos'] = thanos_dict['intelligence']

smartest_hero = max(intelligence_dict, key=intelligence_dict.get)
print(f'Самый умный супергерой - {smartest_hero}')
