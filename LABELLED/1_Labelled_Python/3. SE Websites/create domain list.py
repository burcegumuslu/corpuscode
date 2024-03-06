import csv
import json
you_gov_domain_list = []

import pandas as pd

path_raw_SE = 'SE_domain_list.json'

path_TS = '../../3_Websites/TrustedSources.xlsx'
path_PS = '../../3_Websites/Pseudoscience.csv'

def filter_domains():
    filtered_list = []
    you_gov_domain_list = []
    with open("mainstream domain list 20230711.json") as file:
        se_list = json.load(file)

    for dict in se_list:
        #if dict['count'] > 1:
        if len(dict['source']) > 1:
            filtered_list.append(dict)
    print(len(filtered_list))
    return filtered_list



def create_domain_list(my_list):
    you_gov_domain_list = []
    with open('../../domains/Mainstream yougov list.csv','r') as input_file:  ## If you want to use other domains create a csv file making sure that the domains
            ###################################### are written the first column.

        reader = csv.reader(input_file, delimiter=';')  ## Depending on the csv file, delimiliter might be different, e.g. ';'

        next(reader)  ## This line should be deleted if the csv file doesn't contain any column names.

        for row in reader:
            you_gov_domain_list.append(row[0])

    CAM_list = []

    with open('../../domains/Domains_and_Sources.csv', 'r') as input_file:  ## If you want to use other domains create a csv file making sure that the domains
        ###################################### are written the first column.

        reader = csv.reader(input_file, delimiter=',')  ## Depending on the csv file, delimiliter might be different, e.g. ';'

        next(reader)  ## This line should be deleted if the csv file doesn't contain any column names.

        for row in reader:
            CAM_list.append(row[1])

    get_rid_of = []

    get_rid_of = you_gov_domain_list + ['bing.com', 'google.com', 'google.de', 'bing.de'] + CAM_list

    new_domain_list= []

    for dict in my_list:
        if dict['domain'] not in get_rid_of:
            new_domain_list.append(dict['domain'])

    print(new_domain_list)

    new_domain_list = set(new_domain_list)

    new_domain_list = list(new_domain_list)

    print(len(new_domain_list))


    with open("Mainstream SE List minus Yougov.json", 'w+') as output:
        json.dump(new_domain_list, output)

    return(new_domain_list)





def sanity_check():
    with open("Mainstream SE List minus Yougov.json", 'r') as output:
        new_list = json.load(output)
    print('Sanity check')
    print(new_list)
    print(len(new_list))


my_list = filter_domains()
print(len(my_list))
print(my_list)
#create_domain_list(my_list)


#sanity_check()












def create_domain_inventory():
    with open(path_TS, 'r') as input_file:  
        
        ## If you want to use other domains create a csv file making sure that the domains
            ###################################### are written the first column.

        reader = csv.reader(input_file, delimiter=';')  ## Depending on the csv file, delimiliter might be different, e.g. ';'

        next(reader)  ## This line should be deleted if the csv file doesn't contain any column names.

        for row in reader:
            you_gov_domain_list.append(row[0])


    df = pd.read_csv(path_TS, delimiter=';')


    print(type(df.loc[10].at["source"]))

    print(you_gov_domain_list)


    you_gov_domain_list = you_gov_domain_list +['bing.com', 'google.com', 'google.de', 'bing.de']

    with open("SE_domain_list.json") as file:
        se_list = json.load(file)

    inventory = se_list


    for n in range(0,len(df.index)):
        if any(str(df.loc[n].at["domain"]) == str(dict['domain']) for dict in inventory):
            for dict in inventory:
                if df.loc[n].at["domain"] == str(dict['domain']):
                    source = df.loc[n].at["source"].split('[')[1]
                    source = source.split(']')[0]
                    if ',' in source:
                        dict['source'] = dict['source'] + [source.split(',')[0],source.split(',')[1]]
                        dict['count'] = dict['count'] + 2
                    else:
                        dict['source'] = dict['source'] + [source]
                        dict['count'] = dict['count'] + 1
        else:
            inventory.append({'domain': df.loc[n].at["domain"], 'source': df.loc[n].at["source"]})

    print('inventory')
    print(inventory)

    new_domain_list= []

    for dict in se_list:
        if dict['domain'] not in you_gov_domain_list:
            new_domain_list.append(dict['domain'])

    print(new_domain_list)

    new_domain_list = set(new_domain_list)

    print(len(new_domain_list))

    with open("Domain List SE and YouGov 20230711.json", 'w+') as output:
        json.dump(inventory, output)