from django.db import models

# Create your models here.
class employee(models.Model):
    empid=models.CharField()
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    contact=models.IntegerField()
    position=models.CharField(max_length=50)
    salary=models.CharField()
    Password=models.CharField(max_length=6)

class passwordrest(models.Model):
    email=models.EmailField()
    classotp=models.CharField(max_length=6)


class Query(models.Model):
    employe_mailid= models.EmailField()
    title=models.CharField()
    question = models.TextField()
    reply = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.employee

     
    