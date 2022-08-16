
import json
import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets'



request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, 'html.parser')
for i in soup.find_all("a",href = True):
    print(i['href'])

URL1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.names"
response = requests.get(URL1)
open("test.zip", "wb").write(response.content)
