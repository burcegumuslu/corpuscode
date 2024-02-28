import json
import time
from domainextraction import getDomain

how_many_pages = 6

how_many_results = 40

vaccine_keywords = ['vaccine', 'vaccine side effects', 'vaccine alternatives', 'vaccine contamination', 'vaccine autism',
                    'vaccine immune system', 'vaccine infant',  'vaccine safety', 'vaccine efficacy', 'vaccine clinical trials',
                    'vaccine approval process', 'vaccine children', 'vaccine toxin']




CAM_keywords = ['holistic healing', 'herbal remedies', 'natural immunization', 'boost immune system',
                'homeopathy', 'ayurveda', 'naturopathy', 'aromatherapy', 'spiritual healing ceremony',
                'osteopathy', 'anthroposophic medicine','non-toxic treatments','treatment natural ingredients']




google = "https://www.google.com/"
bing = "https://www.bing.com/"

## Choose search engine
input_search_engine = input('Which search engine do you want to use? Please enter "google" or "bing"').lower()
print(input_search_engine)
##instead of this one can just write:
#input_search_engine = 'google'
#or
##input_search_engine = 'bing'

def set_search_engine(input_search_engine):
    if input_search_engine == 'bing' or input_search_engine == "'bing'":
        search_engine = bing
        return search_engine
    elif input_search_engine == 'google' or input_search_engine == "'google'":
        search_engine = google
        return search_engine
    else:
        input_search_engine = input('Which search engine do you want to use? Please enter EITHER "google" OR "bing"').lower()
        return set_search_engine(input_search_engine)

search_engine = set_search_engine(input_search_engine)

print(search_engine)
if search_engine == bing:
    search_engine_name = 'Bing'
if search_engine == google:
    search_engine_name = 'Google'

print('Search engine: ' + search_engine_name)

from functions import open_browser, browser_search, get_URLs_in, quit
import datetime
from datetime import date
import pytz


def get_search_results(domain_list_unique=None, key_words = CAM_keywords):
    if key_words == CAM_keywords:
        outfile_name = f"search_results_{search_engine_name}_CAM_keywords_{date.today()}.json"
    else:
        outfile_name = f"search_results_{search_engine_name}_vaccine_keywords_{date.today()}.json"
    search_results = []
    for key_word in key_words:
        print('Keyword: ' + key_word)
        key_word_results_list = []
        key_word_results_dict = {}
        search_phrase = key_word
        print('\n Searching for:')
        print(search_phrase)

        ## Opens the browser and the search engine website that was picked
        open_browser(search_engine)

        ## Searches for the search_phrase that is in the "site:example.com keyword" format
        browser_search(search_engine_name, search_phrase)

        ##### Here what is important is running the get_URLs_in function.
        ##### get_URLs_in returns a Boolean function that indicates whether results were removed or not.
        get_URLs_in(search_engine_name, how_many_pages, how_many_results, key_word_results_list)

        ## Timestamp today
        utc_now = datetime.datetime.now(tz=pytz.utc)
        ## Convert UTC to Germany timezone
        germany_tz = pytz.timezone('Europe/Berlin')
        germany_now = utc_now.astimezone(germany_tz)
        ## Format the timestamp string
        timestamp = germany_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')

        ##UPDATE domain_result_dict
        ## domain_result_dict is different for each domain in our domain list
        domain_list = []
        for result in key_word_results_list:
            domain = getDomain(result)
            domain_list.append(domain)
        print(domain_list)
        print('len result list: ', len(key_word_results_list))
        print('len domain list: ', len(domain_list))
        domain_set = set(domain_list)
        print(domain_set)
        print('len domain set: ', len(domain_set))
        domain_dict = []
        for domain in domain_set:
            domain_dict.append({'domain': domain, 'count': domain_list.count(domain)})
        if search_engine == bing:
            key_word_results_dict = {'key_word': key_word, 'results': key_word_results_list, 'domains': domain_dict,
                              'timestamp': timestamp, 'search-engine': search_engine_name}
        if search_engine == google:
            key_word_results_dict = {'key_word': key_word, 'results': key_word_results_list , 'domains': domain_dict,
                                  'timestamp': timestamp, 'search-engine': search_engine_name,}


        ## UPDATE search_results, this is the list which stores all the information
        search_results.append(key_word_results_dict)

        ## To get the results saved in a JSON file:

        with open(outfile_name, "w+") as outfile:
            json.dump(search_results, outfile) #saves the  search_results list as a JSON file. The list is updated
            #### after the search is finished for each domain. So, if there is a problem, the search results from the previous domains
            #### will not be lost

        print(" ")
        print("Results are saved in the file:")
        print(outfile_name)

        print("You will need this file name if you want to continue retrieving results or revise the search results")
        time.sleep(2)

    quit()  # shuts down the entire browser


get_search_results(key_words= CAM_keywords)



#get_search_results(key_words = vaccine_keywords)
