from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import requests
import requests 
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import os

def getShopsData():
        
    filename = os.path.realpath('competitor.xlsx')
    
    df = pd.read_excel(filename, sheet_name='Good competitors')
    counter = 0

    result  = []


    for i in df['Name']:

        try:
            print(counter)
            response = requests.get("https://www.etsy.com/shop/{}".format(i),timeout=1.5)
            tree = html.fromstring(response.content)
            
            
            store_name = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/h1/text()')
            store_label = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/p/text()')
            location = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/span/text()')
            sales = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span[2]/text()')
            all_products = tree.xpath('//*[@id="content"]/div[1]/div[2]/div[2]/span/div[2]/div[1]/div[2]/ul/button[1]/span[2]/text()')
            total_reviews = tree.xpath('//*[@id="reviews"]/div/div/div[2]/div[1]/div[1]/div[3]/text()')
            headers = {
                "access-control-allow-credentials": "true",
                "access-control-allow-headers": "Authorization,Origin, Access-Control-Request-Headers, SERVER_NAME, Access-Control-Allow-Headers, cache-control, token, X-Requested-With, Content-Type, Accept, Connection, User-Agent, Cookie",
                "access-control-allow-methods": "GET,POST,PUT,OPTION",
                "access-control-allow-origin": "https://etsyhunt.com",
                "content-encoding": "gzip",
                "Content-Type": "text/html; charset=UTF-8",
                "date": "Sat, 10 Dec 2022 14:37:08 GMT",
                "vary": "Accept-Encoding",
                "x-guid":"MTY3MDY4NTQxN3wzNjN8MTAyMTExNTI4Mg==",
                "x-pnm": "etsyhunt",
                "authorization": "undefined",
            }
            url = "https://etsyhunt.com/ecommerce/chrome-plug/store-detail"
            data = {
                "store_name": i
            }
            response = requests.get( url=url, data=data, headers=headers,timeout=1.5)
            data_ = response.json()
            
            r_data = {}
            r_data['store_name'] = store_name
            r_data['store_label'] = store_label
            r_data['location'] = location
            r_data['sales'] = sales
            r_data['all_products'] = all_products
            r_data['total_reviews'] = total_reviews
            
            try:
                r_data['sales_7days'] = data_['data']['sales_7days']
            except:
                r_data['sales_7days'] = ""
                
            try:
                r_data['reviews_7days'] = data_['data']['reviews_7days']
            except:
                r_data['reviews_7days'] = ""
                
            try:
                r_data['favorites_7days'] = data_['data']['favorites_7days']
            except:
                r_data['favorites_7days'] = ""
                
                
            try:
                r_data['rating'] = data_['data']['rating'] 
            except:
                r_data['rating'] = "" 
                
            result.append(r_data)
            counter+=1
        except:
            print('skipping timeout reustl')
            continue
        context = {}
        context['message'] = result

    return context

