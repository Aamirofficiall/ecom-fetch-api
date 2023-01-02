from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import os
import re


def Round(value):
  return round(value, 2)
def Average(lst):
    return  sum(lst) / len(lst)



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



def getShopsDataFromEtsyHunt(links):
    
        token = """eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsYW4iOiJlbiIsInZlciI6InNtYiIsInRpbWVzdGFtcCI6MTY3MjYwNDQ4NywiZXhwaXJlIjoxNjcyODYzNjg3LCJ1c2VyX2lkIjoiUzFKblJsaFVhZz09IiwiYXBwbmFtZSI6IkV0c3lIdW50Iiwic3Vic2NyaXB0aW9uIjp7ImlkIjoiMTgyMjcxIiwicGxhbl9pZCI6IjI1MSIsInBsYW5fcHJpY2VfaWQiOiIyNjkiLCJ1c2VyX2lkIjoiMTQ4MzEwNSIsImNoYW5uZWwiOiIwIiwiY2hhbm5lbF9jdXN0X2lkIjoiY3VzX01idmJpY3RKd2hXWVA3IiwiY2hhbm5lbF9zdWJzY3JpcHRpb25fb3Jfb3JkZXJfaWQiOiJzdWJfMUxzaGttSmMxSWFobTJFOVdBZ3U4dGlnIiwiY2hhbm5lbF9zdGF0dXMiOiJhY3RpdmUiLCJjaGFubmVsX2xhc3RfcGF5bWVudF9kYXRlIjoiMCIsImNoYW5uZWxfbGFzdF9wYXltZW50X2Ftb3VudCI6IjAiLCJjaGFubmVsX3N0YXJ0X2F0IjoiMTY3MTAwMDc0MCIsImNoYW5uZWxfY2FuY2VsZWRfYXQiOiIwIiwiY2hhbm5lbF9lbmRfYXQiOiIwIiwicGVyaW9kX3N0YXJ0IjoiMTY2NTczMDM0MCIsInBlcmlvZF9lbmQiOiIxNjczNjc5MTQwIiwicGVyaW9kX2RlbGF5IjoiMCIsImlzX3RyaWFsIjoiMCIsInNjYWxhIjpudWxsLCJsYXN0X3N5bmMiOiIxNjcyNTkwNTUyIiwiY3JlYXRlZF9hdCI6IjIwMjItMTAtMTMgMjM6NTI6MTkiLCJsYXN0X21vZGlmaWVkIjoiMjAyMy0wMS0wMSAwODoyOToxMiIsImNhbmNlbGVkX2F0IjoiMDAwMC0wMC0wMCAwMDowMDowMCIsImVuZGVkX2F0IjoiMDAwMC0wMC0wMCAwMDowMDowMCIsInN0YXR1cyI6IjEiLCJjb3VudHJ5X2NvZGUiOiIwIiwicGF5X3R5cGUiOiIwIiwicHJlX3N1YnNjcmlwdGlvbl9pZCI6IjAiLCJjb2RlIjoiZXRzeV9wbGFuXzNfbW9udGhfMTlfOTkiLCJwbGFuX25hbWUiOiJFdHN5SHVudCBQcm8iLCJpc19yZWN1cmx5IjoiMSIsInByaWNlIjoiMTkuOTkiLCJkZWZhdWx0X3BsYW4iOiJldHN5X3BsYW5fMF9tb250aF8wIiwicGxhbl90eXBlIjoiUHJvIiwicGxhbl9wcmljZSI6eyJpZCI6IjI2OSIsInBsYW5faWQiOiIyNTEiLCJuYW1lIjoiRVRTWS1Qcm8tMTkuOTlVU0QtTW9udGgiLCJ0aXRsZSI6IiIsImNvZGUiOiJldHN5X3BsYW5fM19tb250aF8xOV85OSIsInByaWNlIjoiMTkuOTkiLCJjdXJyZW5jeV90eXBlIjoiMCIsImludGVydmFsIjoiMiIsImludGVydmFsX2NvdW50IjoiMSIsInN0YXR1cyI6IjEiLCJwYXJlbnRfaWQiOiIwIiwiaXNfcmVjdXJseSI6IjEiLCJ0aGVtZV9pbmZvIjoie1widHJpYWxfZGF5c1wiOlwiMVwiLFwidHJpYWxfYW1vdW50XCI6XCIxXCIsXCJjbnlfdHJpYWxfYW1vdW50XCI6XCI2LjVcIixcImJ0bl9ldmVudF90eXBlXCI6XCIxXCIsXCJjb250ZW50X2xpc3RfY29sb3JcIjpcIiNmMTcwM2ZcIixcInByaWNlX3RleHRcIjpcIjE5Ljk5XCIsXCJwcmljZV90ZXh0XzFcIjpcIjE5Ljk5XCIsXCJ0aW1lX3RleHRcIjpcIlxcdTY3MDhcIixcInRpbWVfdGV4dF8xXCI6XCJtb1wiLFwiZGVmYXVsdF9pY29uXCI6XCJlbC1pY29uLXN1Y2Nlc3NcIixcImNvbnRlbnRfbGlzdFwiOlwiXFx1OTAwOVxcdTU0YzFcXHU2NDFjXFx1N2QyMlxcdWZmMWFcXHU0ZTBkXFx1OTY1MFxcblxcdTU1NDZcXHU1NGMxXFx1NTNjYVxcdTVlOTdcXHU5NGZhXFx1Njk5Y1xcdTUzNTVcXHVmZjFhXFx1NTE2OFxcdTkwZThcXHU1YzU1XFx1NzkzYVxcblxcdTVlOTdcXHU5NGZhXFx1NjQxY1xcdTdkMjJcXHVmZjFhXFx1NGUwZFxcdTk2NTBcXG5cXHU1ZTk3XFx1OTRmYVxcdTUyMDZcXHU2NzkwXFx1ZmYxYVxcdTRlMGRcXHU5NjUwXFxuXFx1NTE3M1xcdTk1MmVcXHU4YmNkXFx1NTIwNlxcdTY3OTBcXHVmZjFhXFx1NmJjZlxcdTY1ZTUyMDBcXHU2YjIxXFxuXFx1NjUzNlxcdTg1Y2ZcXHU1MjlmXFx1ODBmZFxcdWZmMWFcXHU2NzAwXFx1NTkxYTI1MDBcXHU0ZTJhXFxuTGlzdGluZ1xcdTRmMThcXHU1MzE2XFx1ZmYxYVxcdTZiY2ZcXHU1OTI5MTAwXFx1NmIyMVxcblxcdTdkMjJcXHU4YmM0XFx1NTI5ZlxcdTgwZmRcXHVmZjFhXFx1NmJjZlxcdTY1ZTU1MDBcXHU2YjIxXFxuXFx1NGU5YVxcdTlhNmNcXHU5MDBhXFx1NjI0YlxcdTVkZTVcXHU1NGMxXFx1ZmYxYVxcdTRlMGRcXHU5NjUwXFxuXFx1NGUwYlxcdTY3YjZcXHU1NTQ2XFx1NTRjMVxcdTkwMDlcXHU1NGMxXFx1ZmYxYVxcdTRlMGRcXHU5NjUwXFxuXFx1NTkxYVxcdTVlOTdcXHU5NGZhXFx1N2VkMVxcdTViOWFcXHVmZjFhMTBcXHU0ZTJhXFx1NWU5N1xcdTk0ZmFcIixcImNvbnRlbnRfbGlzdF8xXCI6XCJQcm9kdWN0IFNlYXJjaDogVW5saW1pdGVkXFxuUHJvZHVjdCBDaGFydDogVW5saW1pdGVkXFxuU2hvcCBTZWFyY2g6IFVubGltaXRlZFxcblNob3AgQW5hbHlzaXM6IFVubGltaXRlZFxcblNob3AgQ2hhcnQ6IFVubGltaXRlZFxcbktleXdvcmQgU2VhcmNoOiAyMDAgRGFpbHlcXG5GYXZvcml0ZXM6IFVwIHRvIDI1MDBcXG5MaXN0aW5nT3B0aW1pemU6IDEwMCBEYWlseVxcbkZvbGxvd3VwUmVtaW5kOiA1MDAgRGFpbHlcXG5BbWF6b24gSGFuZG1hZGU6IFVubGltaXRlZFxcbkluYWN0aXZlIFByb2R1Y3RzOiBVbmxpbWl0ZWRcXG5NdWx0aS1TdG9yZSBCaW5kaW5nOiAxMCBzaG9wc1wiLFwicGxhbl9jdXN0b21fc3R5bGVcIjp7XCJhY3RpdmVcIjpcImZhbHNlXCIsXCJub3JtYWxfYnRuX3RleHRfY29sb3JcIjpcIiNGRkZcIixcIm5vcm1hbF9idG5fYmdfY29sb3JcIjpcIiNmMTcwM2ZcIixcIm5vcm1hbF9ib3JkZXJfY29sb3JcIjpcIiNlYmViZWJcIixcImhvdmVyX2J0bl90ZXh0X2NvbG9yXCI6XCIjRkZGXCIsXCJob3Zlcl9idG5fYmdfY29sb3JcIjpcIiNmMTcwM2ZcIixcImhvdmVyX2JvcmRlcl9jb2xvclwiOlwiI2ViZWJlYlwiLFwiaG92ZXJfc2NhbGVcIjpcIjEwXCIsXCJ1c2luZ19idG5fdGV4dF9jb2xvclwiOlwiI0ZGRlwiLFwidXNpbmdfYnRuX2JnX2NvbG9yXCI6XCIjZjE3MDNmXCIsXCJ1c2luZ19ib3JkZXJfY29sb3JcIjpcIiNlYmViZWJcIn0sXCJ0aGVtZV9zdHlsZVwiOlwiMVwiLFwiY29udGVudF9saXN0X3N0eWxlXCI6XCIyXCIsXCJkZWZhdWx0X2ljb25fY29sb3JcIjpcIiNmMTcwM2ZcIixcInllYXJfc2F2ZV9wcmljZVwiOlwiXCIsXCJpc190cmlhbFwiOjAsXCJ0aXRsZV8xXCI6XCJQcm9cIixcInByaWNlXCI6XCIxOS45OVwiLFwic3ViX3RpdGxlXzFcIjpcIkFkdmFuY2VkIHNlbGVjdGlvblxcbkhlbHBpbmcgbXVsdGktc3RvcmUgc2VsbGVyXFxuXCIsXCJzdWJfdGl0bGVcIjpcIlxcdTU5MWFcXHU1ZTk3XFx1OTRmYVxcXC9cXHU5NGZhXFx1OGQyN1xcdTUzNTZcXHU1YmI2XFx1NWZjNVxcdTkwMDlcXG5cXHU5YWQ4XFx1OTYzNlxcdTkwMDlcXHU1NGMxXFx1NTI5ZlxcdTgwZmRcXHU1MmE5XFx1NjBhOFxcdTU5MjdcXHU1MzU2XCIsXCJ0aXRsZVwiOlwiUHJvXCIsXCJidG5fbmFtZVwiOlwiXFx1N2FjYlxcdTUzNzNcXHU4YmEyXFx1OTYwNVwiLFwiYnRuX25hbWVfMVwiOlwiR0VUXCIsXCJwcmljZV9kZXNcIjpcIlwifSIsImxldmVsIjoiMCIsImlzX2RlZmF1bHRfcGxhbiI6IjAiLCJ0eXBlIjoiMCIsImlzX2RlbGV0ZWQiOiIwIiwiY3JlYXRlZF9hdCI6IjIwMjItMDQtMjggMDE6MTc6NTEiLCJ1cGRhdGVkX2F0IjoiMjAyMi0wOS0yOSAwNzoyMzowOCJ9fX0.SIZjEs6_eUv9vATrUD34Lv3ZAMhFogOEGg-DX6YP8lE"""
        result = []
        
        for link in links:

            store_name = link.link.split('/')[-1]
            url = "https://etsyhunt.com/ecommerce/store/v1_0/basic-info?store_name={}".format(store_name)

            headers = {
                "authorization": token
            }
            querystring = {"store_name":"RedKapokflowers"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            product_analysis = response.json()['data']['product_analysis']['product_list']
            data = {}
            price_list = []
            print(link.link.split('/')[-1])
            print('---------------------------')            
            
            for i in product_analysis:
                price_list.append(float(i['price']))


            # pricing
            
            s = re.sub(r"(?<=\w)([A-Z])", r" \1",store_name)
            store_name_ = s.split('/')[-1]
            data['Store Name'] = store_name_
            data['Max Price'] = Round(max(price_list))
            data['Average Price'] = Round(Average(price_list))
            data['Average Price'] = Round(Average(price_list))
            


            # shipping
            data['Max Shipped Time'] = (response.json()['data']['product_analysis']['shipped_distribute']['max_shipped'])
            data['Min Shipped Time'] = (response.json()['data']['product_analysis']['shipped_distribute']['min_shipped'])
            data['Average Shipped Time'] = (response.json()['data']['product_analysis']['shipped_distribute']['processing_time'])
            category_list = (response.json()['data']['product_analysis']['category_list'])
            data['Category List'] = category_list[0]['name']

            data['Created At']   =(response.json()['data']['basic_info']['created_at'])
            data['Sales Month']  =(response.json()['data']['basic_info']['sales_month'])

            result.append(data)
            
        return result
