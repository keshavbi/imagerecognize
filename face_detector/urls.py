# snippets/urls.py
from django.urls import path,include
# from rest_framework.urlpatterns import format_suffix_patterns
# from admin_app.urlpatterns import format_suffix_patterns
from face_detector import views
# from admin_app import api_views
#App name for view
app_name = 'face_detector'

urlpatterns = [
#Home
        #path('', views.IndexView.as_view(), name='home'),
# API url
        # path('api/v1/posts/', views.PostListView.as_view(), name='list'),
        # path('api-create/', api_views.PostCreateView.as_view(), name='create'),
        # path('api/<int:pk>/', api_views.PostDetailView.as_view(), name='detail'),
        # path('update/<int:pk>/',views.ProjectUpdateView.as_view(), name='update'),
        # path('delete/<int:pk>/',views.ProjectDeleteView.as_view(), name='delete'),
        path('detect/', views.detect, name='detect')
        ]
