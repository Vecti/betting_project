"""
Module dosctring - to fill
"""

from collections import defaultdict
import sys
import pandas as pd
from requests_html import AsyncHTMLSession

country_name = input('Provide country from which you want results:').lower()
country_league_name = {'poland': 'ekstraklasa',
                       'england': 'premier-league',
                       'spain': 'laliga'}
MAIN_URL = 'https://www.flashscore.com/football/'
if country_name in country_league_name:
    country_path = country_name + "/" + country_league_name[country_name]
    url = MAIN_URL + country_path + "/results"
    print(url)
else:
    print('no available input, exit')
    sys.exit()

asession = AsyncHTMLSession()


async def get_scores():
    """
    dostring to fill
    """
    run = await asession.get(url)
    await run.html.arender()
    return run

results = asession.run(get_scores)
results = results[0]

times = results.html.find("div.event__time")
h_team = results.html.find("div.event__participant.event__participant--home")
home_score = results.html.find("div.event__score--home")
a_team = results.html.find("div.event__participant.event__participant--away")
away_score = results.html.find("div.event__score--away")
event_part = results.html.find("div.event__part")

dict_res = defaultdict(list)

for ind in enumerate(times):
    dict_res['times'].append(times[ind].text)
    dict_res['home_teams'].append(h_team[ind].text)
    dict_res['home_score'].append(home_score[ind].text)
    dict_res['away_teams'].append(a_team[ind].text)
    dict_res['away_score'].append(away_score[ind].text)
    dict_res['event_part'].append(event_part[ind].text)

df_res = pd.DataFrame(dict_res)
df_res.to_excel(str(country_name)+'.xlsx')
