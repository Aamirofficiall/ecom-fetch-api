from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  permissions
from .scraper import getEventsData




class get_api_data(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        try:
            
            container_id =request.GET.get('container')
            print(container_id)
            output = getEventsData(container_id)
            return Response(output)
        except:
            return Response({"error":"token update"})
                    

    