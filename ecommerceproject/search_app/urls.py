
#from django.urls import path
#from . import views
#app_name='search_app'

#urlpatterns = [
 #       path('',views.searchResult,name='searchResult'),
  #    ]

from django.urls import path,re_path
from . import views

app_name = 'search_app'

urlpatterns = [
        path('', views.searchResult, name='searchResult'), #using re_path as path does'nt allow use of regular expressions and we are using regex here so django does'nt get confuse with patterns
]
