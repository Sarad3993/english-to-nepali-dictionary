from django.urls import path 
from .views import *
from django.conf.urls.static import static 
from EngToNepDict.settings import DEBUG, MEDIA_ROOT,MEDIA_URL 

app_name = 'mydictapp'

urlpatterns = [
    path('',engtonepdict,name='engtonepdict'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)