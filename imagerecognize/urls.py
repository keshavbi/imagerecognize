"""imagerecognition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path,include
from formapp import views
from admin_app import views as adminAppView
from face_detector import views as detector

urlpatterns = [
    #Home Page url
    path('', adminAppView.IndexView.as_view(),name='home'),
    #Admin url
    path('admin/', admin.site.urls),
    # For formapp
    path('formapp/', include('formapp.urls')),
    # For admin_app
    path('admin-app/', include('admin_app.urls')),

    #Face Detector
    #path('face_detection/detect/', detector.detect),
    path('face-detector/', include('face_detector.urls')),
]



# Face Detector
# from django.conf.urls import patterns, include, url
# #from django.contrib import admin
#
# urlpatterns += patterns('',
#     # Examples:
#
#     url(r'^face_detection/detect/$', 'face_detector.views.detect'),
#
#     # url(r'^$', 'cv_api.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# )
