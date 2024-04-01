
from django.contrib import admin
from django.urls import path
from SecurityCamera.views import ProcessVideo, webcam_feed 
from RestAPI.views import your_model_view,Result


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', ProcessVideo ,name='hello'),
    path('webcam_feed/', webcam_feed, name='webcam_feed'),
    path('MyAPI/', your_model_view, name='your_model-view'),
    path('Result/', Result, name='Result'),
]
