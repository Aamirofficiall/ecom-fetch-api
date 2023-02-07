from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  permissions
from .scraper import getShopsData,getProductData
from .models import *
import pandas as pd
import os



class get_api_data(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        # try:
            filename = os.path.realpath('competitor.xlsx')
            df = pd.read_excel(filename, sheet_name='Good competitors')

            # for i in df['Store Link']:
            #     print(i)
            #     CompetitorLink.objects.get_or_create(link=i)
                
            links = CompetitorLink.objects.filter()
            output = getShopsData(links)
            return Response(output)
        # except:
        #     return Response({"message":"Error Occu

class get_api_data_products(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        # try:
            links = ProductsLink.objects.filter()
            output = getProductData(links)
            return Response(output)
        # except:
        #     return Response({"message":"Error Occured"})
     