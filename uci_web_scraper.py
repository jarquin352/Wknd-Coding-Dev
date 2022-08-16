import json
import os.path #os.path.exists(path_to_file)
import requests
import re
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets'

def extract_contents(name_url):
    result_lst = []
    url = name_url
    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.find_all("a",href = True):
        #print(i['href'])
        result_lst.append(i['href'])
    return result_lst

# def update_datasets():

############################################################################################################################################################

add_to = ''
input_url = 'https://archive.ics.uci.edu/ml/'
lst_dt = []
lst_dt = extract_contents(url)

new_lst_dt = []

for i in range(0,len(lst_dt)):
    str_curr = re.search('datasets',lst_dt[i], re.I)
    if str_curr == None or str_curr == 'datasets.php':
        continue
    new_lst_dt.append(input_url+lst_dt[i])

#list to set to remove duplicates.
new_lst_dt = list(set(new_lst_dt).copy())

with open('dataset_links.txt','w') as f:
    for i in new_lst_dt:
        f.write(i)
        f.write('\n')
