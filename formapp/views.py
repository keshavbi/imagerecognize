from django.shortcuts import render

from django.http import HttpResponse,HttpRequest,JsonResponse
# from ipaddr import client_ip
from django.urls import reverse, reverse_lazy
# Create your views here.



# Import for CURD:
from . import models
from django.views.generic import (
        View, TemplateView,
        ListView, DetailView,
        CreateView, UpdateView,
        DeleteView
)


# """
# Upload Form torecognize
# """

from django.views.generic.edit import FormView
from .forms import FileFieldForm
from django.urls import reverse

#Image torecognize
from imageai.Prediction.Custom import ModelTraining
# model_trainer = ModelTraining()
# model_trainer.setModelTypeAsResNet()
# model_trainer.setDataDirectory("media")
# model_trainer.trainModel(num_objects=10, num_experiments=200, enhance_data=True, batch_size=32, show_network_summary=True)
#Image torecognize end

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'formapp/new_form.html'  # Replace with your template.
    # success_url = 'formapp:index")'  # Replace with your URL or reverse().


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        return HttpResponse(files)
        # print("Hi upload")
        if form.is_valid():
            for f in files:
        # Do something with each file.

                return HttpResponse(f)
        #return self.form_valid(form)
                return reverse("formapp:index")
        else:
            # return self.form_invalid(form)
            return reverse("formapp:index")



#Form Field upload_to
#from django.views.generic.edit import FormView
#from .forms import FileFieldForm
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

# """
# Upload Form torecognize
# """

class IndexView(ListView):
    context_object_name = 'images'
    model = models.ImageDetail
    template_name = 'formapp/index.html'

class FormappView(CreateView):
    fields = ('title','image','status')
    model = models.ImageDetail
    template_name = 'formapp/form.html'

# POST Request
    #def post(self, request, *args, **kwargs):

    #template_name = 'formapp/form.html'
# def Index(request):
#     return render(request,'formapp/index.html')
#
# def Formapp(request):
#     return render(request,'formapp/form.html')
