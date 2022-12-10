from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  permissions
from .scraper import getShopsData




class get_api_data(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        # try:
            
            output = getShopsData()
            return Response(output)
        # except:
        #     return Response({"message":"Error Occured"})
                    

    