import json
import requests
import re
import os.path
from alive_progress import alive_bar #https://github.com/rsalmei/alive-progress
from time import sleep
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets'
input_url = 'https://archive.ics.uci.edu/ml/'

def lst_to_dict(l1,l2):
    ret1_dict = {}
    if len(l1) != len(l2):
        return ret1_dict
    else:
        for i in range(len(l1)):
            ret1_dict[l1[i]] = l2[i]
        return ret1_dict

def extract_contents(name_url):
    result_lst = []
    url = name_url
    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.find_all("a",href = True):
        result_lst.append(i['href'])
    #return result_lst
    new_lst_dt = []
    for i in range(0,len(result_lst)):
        str_curr = re.search('datasets/',result_lst[i], re.I)
        if str_curr == None or str_curr == 'datasets.php?':
            continue
        new_lst_dt.append(input_url+result_lst[i])
    #list to set to remove duplicates.
    new_lst_dt = list(set(new_lst_dt).copy())
    #return new_lst_dt

    second_lst_url = []
    with alive_bar(len(new_lst_dt), bar = 'filling') as bar:
        for j in range(len(new_lst_dt)): #range(len(ds_links)):
            newurl = new_lst_dt[j]
            content_newurl = requests.get(newurl).content
            soup_newurl = BeautifulSoup(content_newurl,'html.parser')
            links_with_text = [a['href'] for a in soup_newurl.find_all('a',href = True) if a.text]
            tmp_holder = links_with_text[9].strip('..')
            second_lst_url.append(tmp_holder)
            sleep(0.03)
            bar()
    final_dict = lst_to_dict(new_lst_dt,second_lst_url)
    
    return final_dict

def update_dict():
    lst_to_update = extract_contents(url)
    with open('dataset_links.txt','w') as f:
        for i in lst_to_update:
            f.write(i)
            f.write('\n')















if __name__ == "__main__":
    dict_test = extract_contents(url)
    with open('ds_links.json','w',encoding = 'utf-8') as f:
        json.dump(dict_test,f,ensure_ascii=False,indent=4)
    # #user input dynamic code here
    # if os.path.isfile('./dataset_links.txt'):
    #     ds_links = open('dataset_links.txt').read().splitlines()
    # else:
    #     update_dict()
    #     ds_links = open('dataset_links.txt').read().splitlines()

