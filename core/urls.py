
from django.contrib import admin
from django.urls import path
from scrappingapp.views import get_api_data
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', get_api_data.as_view()),
    
    
]
