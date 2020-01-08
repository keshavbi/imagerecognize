# snippets/urls.py
from django.urls import path,include
# from rest_framework.urlpatterns import format_suffix_patterns
# from admin_app.urlpatterns import format_suffix_patterns
from admin_app import views
from .api import api_views,detect_views
#App name for view
app_name = 'admin_app'

urlpatterns = [
#Home
        path('', views.IndexView.as_view(), name='home'),
# API url
        path('api/v1/detect', detect_views.detect, name='detector'),
        path('api/v1/posts/', views.PostListView.as_view(), name='list'),
        path('api-create/', api_views.PostCreateView.as_view(), name='create'),
        path('api/<int:pk>/', api_views.PostDetailView.as_view(), name='detail'),
        path('update/<int:pk>/',views.ProjectUpdateView.as_view(), name='update'),
        path('delete/<int:pk>/',views.ProjectDeleteView.as_view(), name='delete'),

# Project URL
        path('project-create/', views.ProjectCreateView.as_view(), name='project-create'),
        path('project-list/', views.ProjectListView.as_view(), name='project-list'),
        path('project-list/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
        path('project-update/<int:pk>/', views.ProjectUpdateView.as_view(), name='project-update'),
        path('project-delete/<int:pk>/', views.ProjectDeleteView.as_view(), name='project-delete'),

# Employee URL
        path('employee-create/', views.EmployeeCreateView.as_view(), name='employee-create'),
        path('employee-list/', views.EmployeeListView.as_view(), name='employee-list'),
        path('employee-list/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
        path('employee-update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee-update'),
        path('employee-delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    #
    # path('', views.ProjectListView.as_view(),name='list'),
    # path('<int:pk>/',views.ProjectDetailView.as_view(), name='detail'),
    # path('create/', views.ProjectCreateView.as_view(), name='create'),
    # path('update/<int:pk>/',views.ProjectUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/',views.ProjectDeleteView.as_view(), name='delete'),
    #
    # # Student
    # path('employee-list/',views.EmployeeListView.as_view(), name='employee-list'),
    # path('employee-list/<int:pk>/',views.EmployeeDetailView.as_view(), name='employee-detail'),
    # path('employee-create', views.EmployeeCreateView.as_view(), name='employee-create')

]

# urlpatterns = format_suffix_patterns(urlpatterns)
