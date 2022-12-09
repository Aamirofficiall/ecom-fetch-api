from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import requests
   
def getEventsData(container_id):
    
    URL= "https://api.inttra.com/auth"
    data = {"grant_type": "password",
        "username": "export@deallogusa.com",
        "password": "Rodrigoricardo1"
        }
    headers={ 'Content-Type':'application/json'}
    r = requests.post(URL,headers=headers,json=data)
    print(r.json())
    token = r.json()['access_token']
    
    URL = "https://api.inttra.com/visibility/containers?broad_search_key={}".format(container_id)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
 
    headers={ 'Content-Type':'application/json','Authorization': f'Bearer {token}'}
    r = requests.get(URL,headers=headers)
    return r.json()
