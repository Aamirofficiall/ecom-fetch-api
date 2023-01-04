
from django.contrib import admin
from django.urls import path
from scrappingapp.views import *
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', get_api_data.as_view()),
    # path('api_from_etsy_hunt/', get_api_data_from_etsy_hunt.as_view()),
]
