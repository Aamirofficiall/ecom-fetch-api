from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import requests
   
def getEventsData(container_id):
    URL = "https://api.inttra.com/visibility/containers?broad_search_key={}".format(container_id)
    print(URL)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    url = 'https://login.inttra.com/'
    values = {
        'email': 'export@deallogusa.com',
        'password': 'Rodrigoricardo1'
    }
    token = '2a7b6f40-251d-4127-b4c2-bfb99c87b7a9'
    headers={ 'Content-Type':'application/json','Authorization': 'Bearer 2a7b6f40-251d-4127-b4c2-bfb99c87b7a9'}
    r = requests.get(URL,headers=headers)
    return r.json()
