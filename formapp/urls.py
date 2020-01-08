from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from admin_app.urlpatterns import format_suffix_patterns
from formapp import views
#from .api import api_views
#App name for view
app_name = 'formapp'
#Form Image sattings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('image-list', views.IndexView.as_view(), name='index'),
    path('create', views.FormappView.as_view(), name='create'),
    path('new-form', views.FileFieldView.as_view(), name='newform'),
]

#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
