import json
import requests
from bs4 import BeautifulSoup

#function takes in a bs4 data structure & turns it into a dict....
def bs4_to_dict(name1,val1):
    ret_dict = {}
    l1 = []
    l2 = []
    if len(name1) != len(val1):
        return ret_dict
    else:
        for i in name1:
            l1.append(i.text)
        for j in val1:
            l2.append(j.text)
        for k in range(len(name1)):
            ret_dict[l1[k]] = l2[k]
    return ret_dict

def lst_to_dict(l1,l2):
    ret1_dict = {}
    if len(l1) != len(l2):
        return ret1_dict
    else:
        for i in range(len(l1)):
            ret1_dict[l1[i]] = l2[i]
        return ret1_dict

#initializing all needed data collection using bs4
url = "https://www.bu.edu/president/boston-university-facts-stats/"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

first_fact = {}
second_fact = {}

#obtains the first set of facts, as it seems there are other facts NOT contained in facts-wrapper class....
facts_section = soup.body.section
facts_secton_text = facts_section

#other facts in the bottom of the html file...
facts_section_other = soup.find_all(class_ = 'list-item')

#finding all related facts for all facts pertaining to the class facts section(first 3 facts)
type_fact = facts_section.find_all("h2")
val_fact = facts_section.find_all('h4')

#first_facts stored, will merge later...
first_fact = bs4_to_dict(val_fact,type_fact)
l1 = []
l2 = []

#extracting name of fact and value from facts_section_other
for i in facts_section_other:
    l1.append(i.contents[1].text)
    l2.append(i.contents[3].text)

#merging the first and second dict
second_fact = lst_to_dict(l1,l2)
final_fact = {**first_fact,**second_fact}

#dumping into a JSON file

with open('merged_facts.json','w',encoding='utf-8') as f:
    json.dump(final_fact,f,ensure_ascii=False,indent=4)
