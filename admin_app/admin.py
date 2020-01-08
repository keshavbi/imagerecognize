from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin):

    #Change Order of fields
    fields = ['release_year', 'title', 'length']
    #Search enable and apply on fields
    search_fields = ['title','length']
    #filter on these fields
    list_filter = ['release_year','length','title']
    #Display of these fields
    list_display = ['title','release_year','length']
    # Editable in list display fields
    list_editable = ['length']

class CustomerMovi(admin.ModelAdmin):
    #Change Order of fields
    fields = ['first_name','last_name','phone']
    #Search enable and apply on fields
    search_fields = ['first_name','last_name','phone']
    #filter on these fields
    list_filter = ['first_name','last_name','phone']
    #Display of these fields
    list_display = ['first_name','last_name','phone']

#project
class ProjectImp(admin.ModelAdmin):
    #Change Order of fields
    fields = ['name','manager','location']
    #Search enable and apply on fields
    search_fields = ['name','manager','location']
    #filter on these fields
    list_filter = ['name','manager','location']
    #Display of these fields
    list_display = ['name','manager','location']

#student
class EmployeeProject(admin.ModelAdmin):
    #Change Order of fields
    fields = ['name','age','project']
    #Search enable and apply on fields
    search_fields = ['name','age','project']
    #filter on these fields
    list_filter = ['name','age','project']
    #Display of these fields
    list_display = ['name','age','project']

#register model
admin.site.register(models.Customer,CustomerMovi)
admin.site.register(models.Movie, MovieAdmin)

admin.site.register(models.Project,ProjectImp)
admin.site.register(models.Employee, EmployeeProject)
