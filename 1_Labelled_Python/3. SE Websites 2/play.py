import json

#with open('mainstream list.json', 'r') as f:
 #   my_list = json.load(f)
#
#print(len(my_list))

#new = []

#for dic in my_list:
 #   if dic['count'] > 2 and len(dic['source']) > 1:
  #      new.append(dic)
#print(len(new))
import csv
import pandas as pd
with open("/Users/burce/Desktop/corpus/domains/Domains_and_Sources.csv") as file:
    #CAM_dom_list = csv.reader(file)
    CAM_dom_list = pd.read_csv(file)

CAM_domain_dict_list = []
for index, row in CAM_dom_list.iterrows():
    dom_dict = {'domain': row['domain'], 'source': row['source'], 'corpus': 'CAM'}
    CAM_domain_dict_list.append(dom_dict)


print(CAM_domain_dict_list)

with open('CAM domain list.json', 'w+') as output:
    json.dump(CAM_domain_dict_list, output)