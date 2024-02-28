import datetime
import traceback
from datetime import date
import pytz

import json

import lxml
from goose3 import Goose
from goose3 import Configuration

#url = "https://blogs.mercola.com/sites/vitalvotes/archive/2023/04/19/fda-_1820_simplifies_1920_-recommendations-for-covid19-bivalent-jabs.aspx"
#data = [{"result_id": "199011", "URL": "https://medicalkidnap.com/2021/05/", "source": ["bing"], "scraped": False}, {"result_id": "199012", "URL": "https://medicalkidnap.com/2022/06/19/warning-pfizer-lied-about-results-in-covid-19-vaccine-trials-for-babies-and-toddlers/", "source": ["google"], "scraped": False}, {"result_id": "199013", "URL": "https://medicalkidnap.com/news/", "source": ["bing"], "scraped": False}]


import json

with open("../../searches/mainstream/20230706 MBIS_MSHC_MTOX_MTNI_MNTT_MANT_MOST_MARO_MAYU_MNAT_MHOM_MHER_MHOH_MNIM_MCHI_MVAP_MVCT_MVEF_MVAS_MVAI_MVIS_MVAU_MVCO_MVAL_MVSE_MVAC_search_results_for_scrape.json", "r") as f:
    data = json.load(f)

config = Configuration()
config.browser_user_agent = 'We are retrieving content for non-commercial academic purposes. Contact: cmmock23@gmail.com'
###

g = Goose(config)

#g = Goose()

##Note: IT IS NORMAL TO GET SOME ERRORS IN THE BEGINNING.


counter = 0
for dictionary in data:
    counter += 1
    URL = dictionary['URL']
    if dictionary['scraped'] == False and dictionary['scrape_attempt'] == False:
        if 'second_scrape_attempt' not in dictionary:
            try:
                ## Timestamp today
                utc_now = datetime.datetime.now(tz=pytz.utc)
                ## Convert UTC to Germany timezone
                germany_tz = pytz.timezone('Europe/Berlin')
                germany_now = utc_now.astimezone(germany_tz)
                ## Format the timestamp string
                timestamp = germany_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')
                item_dict = {'result_id': dictionary['result_id'], 'URL': URL, 'timestamp': timestamp, 'personal_data_cleaned': False}
                article = g.extract(url=URL)
                infos = article.infos
                infos['meta']['website_keywords'] = infos['meta'].pop('keywords')
                item_dict.update(infos)
                item_dict.update({'raw_html': article.raw_html})
                dictionary['scraped'] = True
                dictionary['scrape_attempt'] = True
                dictionary.update({'second_scrape_attempt': True})
                with open(f'../../scraped/mainstream scraped/{dictionary["result_id"]}.json', 'w+') as output_file:
                    json.dump(item_dict, output_file)
                with open('../../searches/mainstream/20230706 MBIS_MSHC_MTOX_MTNI_MNTT_MANT_MOST_MARO_MAYU_MNAT_MHOM_MHER_MHOH_MNIM_MCHI_MVAP_MVCT_MVEF_MVAS_MVAI_MVIS_MVAU_MVCO_MVAL_MVSE_MVAC_search_results_for_scrape.json', 'w+') as output_file:
                    json.dump(data, output_file)
                if counter % 200 == 0:
                    with open(f'../../searches/mainstream/20230706 MBIS_MSHC_MTOX_MTNI_MNTT_MANT_MOST_MARO_MAYU_MNAT_MHOM_MHER_MHOH_MNIM_MCHI_MVAP_MVCT_MVEF_MVAS_MVAI_MVIS_MVAU_MVCO_MVAL_MVSE_MVAC_search_results_for_scrape_{timestamp}_{dictionary["result_id"]}.json', 'w+') as backup_file:
                        json.dump(data, backup_file)
                print('Finished with', URL)
            except Exception as e:
                dictionary['scrape_attempt'] = True
                dictionary.update({'second_scrape_attempt': False})
                print("There was an error with scraping", URL)
                print(f"Error: {e}")
                traceback.print_exc()




# import requests-ÄPÖOL
# from bs4 import BeautifulSoup
#
# the_URL = "https://www.actualized.org/forum/topic/71016-i-want-to-get-the-covid-19-vaccine-but-i%E2%80%98m-hesitant-confused-looking-for-clarity/"
# video_url = "https://freeworldnews.tv/watch?id=6164bd321648ca3e25fb2fd6"
# response = requests.get(video_url)
# soup = BeautifulSoup(response.content, 'html.parser')
#
# #body main div
#
# ps = soup.select('.css-jgvb17 p')
# for p in ps:
#     text = p.text
#     print(text)