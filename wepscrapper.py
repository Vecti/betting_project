from requests_html import AsyncHTMLSession
from collections import defaultdict
import pandas as pd 

country_name = input('Provide country from which you want results:').lower()
country_league_name = {'poland': 'ekstraklasa',
                       'england': 'premier-league',
                       'spain': 'laliga'}
main_url = 'https://www.flashscore.com/football/'
if country_name in country_league_name:
    country_path = country_name + "/"+ country_league_name[country_name]
    url = main_url + country_path +"/results"
    print(url)
else:
    print('no available input, exit')
    exit()



asession = AsyncHTMLSession()

async def get_scores():
    r = await asession.get(url)
    await r.html.arender()
    return r

results = asession.run(get_scores)
results = results[0]

times = results.html.find("div.event__time")
home_teams = results.html.find("div.event__participant.event__participant--home") 
home_score = results.html.find("div.event__score--home")
away_teams = results.html.find("div.event__participant.event__participant--away")
away_score = results.html.find("div.event__score--away")
event_part = results.html.find("div.event__part")



dict_res = defaultdict(list)

for ind in range(len(times)):
    dict_res['times'].append(times[ind].text)
    dict_res['home_teams'].append(home_teams[ind].text)
    dict_res['home_score'].append(home_score[ind].text)
    dict_res['away_teams'].append(away_teams[ind].text)
    dict_res['away_score'].append(away_score[ind].text)
    dict_res['event_part'].append(event_part[ind].text)

df_res = pd.DataFrame(dict_res)

df_res.to_excel(str(country_name)+'.xlsx')