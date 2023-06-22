from django.db import models

# Create your models here.
class reg_tb1(models.Model):
    fn=models.CharField(max_length=50)
    pn=models.IntegerField()
    em=models.EmailField()
    ps=models.CharField(max_length=8)
    cps=models.CharField(max_length=8)
    to=models.CharField(max_length=20)
class tra_tb1(models.Model):
    tp=models.CharField(max_length=15)
    tm=models.FileField(upload_to="pictures")
class trb_tb1(models.Model):
    m=models.CharField(max_length=15)
    t=models.FileField(upload_to="pictures")
    

