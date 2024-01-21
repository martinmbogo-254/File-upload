from django.db import models

# Create your models here.
  
class Client(models.Model):
    name = models.CharField(max_length=255)
    mobile= models.IntegerField(max_length = 12)
    veh_reg = models.CharField(max_length=20)
    profile_pic = models.FileField(default='profile_imgs/default.png',upload_to='profile_imgs/')

    def __str__(self):
            return self.name
    

class File(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='file')
    name = models.CharField(max_length=255,blank=True)
    file = models.FileField(upload_to='files/',blank=True)
    
    def __str__(self):
        return self.name
  