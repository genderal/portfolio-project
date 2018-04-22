from django.db import models
from datetime import datetime
class Blog(models.Model):
    my_status=models.CharField(max_length=1000)
    image=models.ImageField(upload_to= 'blog_images/')
    title=models.CharField(max_length=255,blank=True)
    pub_date=models.DateTimeField(default=datetime.now(),blank=True)



    # Create your models here.
