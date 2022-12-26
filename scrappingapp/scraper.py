from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import requests
import requests 
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import os

def getShopsData(links):
        
    filename = os.path.realpath('competitor.xlsx')
    
    df = pd.read_excel(filename, sheet_name='Good competitors')
    counter = 0

    result  = []


    for link in links:
        # try:
            print(counter)

            try:
                response = requests.get(link.link,timeout=3.5)
            except:
                continue
            tree = html.fromstring(response.content)
            
            
            store_name = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/h1/text()')
            store_label = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/p/text()')
            location = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/span/text()')
            sales = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span[2]/text()')
            all_products = tree.xpath('//*[@id="content"]/div[1]/div[2]/div[2]/span/div[2]/div[1]/div[2]/ul/button[1]/span[2]/text()')
            total_reviews = tree.xpath('//*[@id="reviews"]/div/div/div[2]/div[1]/div[1]/div[3]/text()')
            headers = {
                    "method": "POST",
                    "path": "/ecommerce/chrome-plug/store-detail",
                    "scheme": "https",
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-PK,en-US;q=0.9,en;q=0.8",
                    "authorization": "undefined",
                    "content-length": "236",
                    "content-type": "application/json",
                    "origin": "https://etsyhunt.com",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "macOS",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                    "access-control-allow-credentials": "true",
                    "access-control-allow-headers": "Authorization,Origin, Access-Control-Request-Headers, SERVER_NAME, Access-Control-Allow-Headers, cache-control, token, X-Requested-With, Content-Type, Accept, Connection, User-Agent, Cookie",
                    "access-control-allow-methods": "GET,POST,PUT,OPTION",
                    "access-control-allow-origin": "https://etsyhunt.com",
                    "content-encoding": "gzip",
                    "Content-Type": "text/html; charset=UTF-8",
                    "date": "Sat, 25 Dec 2022 14:37:08 GMT",
                    "vary": "Accept-Encoding",
                    "x-guid":"MTY3MDY4NTQxN3wzNjN8MTAyMTExNTI4Mg==",
                    "x-pnm": "etsyhunt",
                    "authorization": "undefined",
                
            }
            url = "https://etsyhunt.com/ecommerce/chrome-plug/store-detail"
            print(link.link.split('/')[-1])
            print('---------------------------')
            data = {
                "store_name": link.link.split('/')[-1],
                "has_login": "1",
                "validate": "0613aDyAdVPz2ZVjv063WVfr0vQOj7RM4CvME4qZcCq3gmps"
            }
            

            try:
                response = requests.get( url=url, data=data, headers=headers,timeout=3.5)
                print(response.json())
            except:
                continue
            data_ = response.json()
            
            r_data = {}
            r_data['store_name'] = store_name
            r_data['store_label'] = store_label
            r_data['location'] = location
            r_data['all_products'] = all_products
            
            try:
                r_data['Sales 7 Days'] = data_['data']['sales_7days']
            except:
                r_data['Sales 7 Days'] = ""
                
            try:
                r_data['Reviews 7 Days'] = data_['data']['reviews_7days']
            except:
                r_data['Reviews 7 Days'] = ""
                
            try:
                r_data['Fav 7 Days'] = data_['data']['favorites_7days']
            except:
                r_data['Fav 7 Days'] = ""
                
                
            try:
                r_data['Rating'] = data_['data']['rating'] 
            except:
                r_data['Rating'] = ""
                
                
                 
            try:
                r_data['Total Sales'] = data_['data']['store_sales'] 
            except:
                r_data['Total Sales'] = sales
                
                
            # store_reviews
            # try:
            #     r_data['store_reviews'] = data_['data']['store_reviews'] 
            # except:
            r_data['Total Reviews'] = total_reviews 

            # category
            try:
                r_data['Category'] = data_['data']['category'] 
            except:
                r_data['Category'] = ""
                
                
                
            result.append(r_data)
            counter+=1

            context = result
            
            

    return context

