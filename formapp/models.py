from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class ImageDetail(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='formapp/images', blank=True)
    status = models.BooleanField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        #return self.text
        return "Name: {}, id{}".format(self.title, self.id)

    def get_absolute_url(self):
        return reverse("formapp:index")
        #return reverse("formapp:index",kwargs={'pk':self.pk})
