import json

files = ['search_results_Bing_vaccine_keywords_2023-07-10.json', 'search_results_Google_vaccine_keywords_2023-07-10.json',
         'search_results_Bing_CAM_keywords_2023-07-10.json', 'search_results_Google_CAM_keywords_2023-07-11.json']

def inspect(file):
    with open(file, 'r') as file:
        dicts = json.load(file)
        domain_dict_list = []
    print(file)
    for dict in dicts:
        print(dict["key_word"])
        print("# results", len(dict["results"]))
        print("# domains", len(dict["domains"]))



def merge(file):
    with open(file, 'r') as file:
        dicts = json.load(file)

    domain_dict_list = []

    for dict in dicts:
        for domain in dict['domains']:
            if not any(do['domain'] == domain['domain'] for do in domain_dict_list):
                domain['source'] = [[dict["search-engine"], dict["key_word"]]]
                domain['corpus'] = 'mainstream'
                domain_dict_list.append(domain)
            else:
                for do in domain_dict_list:
                    if do['domain'] == domain['domain']:
                        do['count'] = do['count'] + domain['count']
                        if [dict["search-engine"], dict["key_word"]] not in do['source']:
                            do['source'].append([dict["search-engine"], dict["key_word"]])

    with open('mainstream domain list 20230711.json', 'w+') as output:
        json.dump(domain_dict_list, output)

    print(len(domain_dict_list))

for el in files:
    merge(el)
    #inspect(el)