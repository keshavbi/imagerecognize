from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
# from ipaddr import client_ip
from django.urls import reverse, reverse_lazy
# from .serializers import SnippetSerializer
"""
Start API

"""
from .models import Post
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

# class PostCreateView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#
#     def create(self, request, *args, **kwargs):
#         super(PostCreateView, self).create(request, args, kwargs)
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully created",
#                     "result": request.data}
#         return Response(response)
#
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#
#     def retrieve(self, request, *args, **kwargs):
#         super(PostDetailView, self).retrieve(request, args, kwargs)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         data = serializer.data
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully retrieved",
#                     "result": data}
#         return Response(response)
#
#     def patch(self, request, *args, **kwargs):
#         super(PostDetailView, self).patch(request, args, kwargs)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         data = serializer.data
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully updated",
#                     "result": data}
#         return Response(response)
#
#     def delete(self, request, *args, **kwargs):
#         super(PostDetailView, self).delete(request, args, kwargs)
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully deleted"}
#         return Response(response)


"""
End API

"""



from django.views.generic import (
        View, TemplateView,
        ListView, DetailView,
        CreateView, UpdateView,
        DeleteView
)
# Import from Current App like "basic_app"
from . import models


class IndexView(TemplateView):
    template_name = 'admin_app/index.html'
    # return

class ProjectListView(ListView):
    # Return Default "school_list" modelName concat with list, we can Change by
    context_object_name = 'projects'
    model = models.Project


class ProjectDetailView(DetailView):
    context_object_name = 'project_detail'
    model = models.Project
    template_name = 'admin_app/project_detail.html'

class ProjectCreateView(CreateView):
    fields = ('name','manager', 'location')
    model = models.Project
    template_name = 'admin_app/project_form.html'

class ProjectUpdateView(UpdateView):
    fields = ('name','manager')
    model = models.Project

class ProjectDeleteView(DeleteView):
    model = models.Project
    # return redirect('basic_app:lst')
    success_url = reverse_lazy('admin_app:projecct-list')


#Students
class EmployeeListView(ListView):
    context_object_name = 'employee_list'
    model = models.Employee

class EmployeeDetailView(DetailView):
    context_object_name = 'employee_detail'
    model = models.Employee


class EmployeeCreateView(CreateView):
    fields = ('name','age','project')
    model = models.Employee
    template_name = 'admin_app/employee_form.html'
class EmployeeUpdateView(UpdateView):
    fields = ('name','age', 'project')
    model = models.Employee

class EmployeeDeleteView(DeleteView):
    model = models.Employee
    # return redirect('basic_app:lst')
    success_url = reverse_lazy('admin_app:employee-list')
