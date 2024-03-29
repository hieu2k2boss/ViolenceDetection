
from django.contrib import admin
from django.urls import path
from SecurityCamera.views import ProcessVideo, webcam_feed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', ProcessVideo ,name='hello'),
    path('webcam_feed/', webcam_feed, name='webcam_feed'),
]
