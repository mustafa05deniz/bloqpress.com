from django.db import models
from redactor.fields import RedactorField
from django.contrib.auth.models import User

class catagory(models.Model):
    title=models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.title

class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    resim=models.ImageField(upload_to="tmp/")
    Katagory=models.ForeignKey(catagory)
    zaman=models.DateTimeField(null=True)
    short_text = RedactorField(
    verbose_name=u'Text',
    redactor_options={'lang': 'en', 'focus': 'true'},
    upload_to='tmp/',
    allow_file_upload=True,
    allow_image_upload=True
)
    def __unicode__(self):
        return self.title
    
class Resim_Katalogu(models.Model):
    resim1 = models.ImageField(upload_to="tmp/")

class Sozler(models.Model):
    text=models.CharField(max_length=1000)
    
    
    

class raporlar(models.Model):
    title=models.CharField(max_length=100)
    text=models.CharField(max_length=1000)
    
    def __unicode__(self):
        return self.title
    
    
class PageCounter(models.Model):
    sayi_ismi = models.CharField(max_length=100)
    sayi=models.IntegerField()
    
    def __unicode__(self):
        return self.sayi_ismi
    

class Gelen_yazilar(models.Model):
    gonderen_adi=models.CharField(max_length=30)
    text=models.TextField(max_length=100000)
    
    def __unicode__(self):
        return self.gonderen_adi
    
class Testler(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    resim=models.ImageField(upload_to="tmp/")
    short_text = RedactorField(
    verbose_name=u'Text',
    redactor_options={'lang': 'en', 'focus': 'true'},
    upload_to='tmp/',
    allow_file_upload=True,
    allow_image_upload=True
)
    def __unicode__(self):
        return self.title
