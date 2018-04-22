from django.db import models
from datetime import datetime
class Blog(models.Model):
    title=models.CharField(max_length=255,blank=True)
    pub_date=models.DateTimeField(default=datetime.now(),blank=True)
    my_status=models.TextField()
    image=models.ImageField(upload_to= 'blog_images/')

    # Create your models here.
