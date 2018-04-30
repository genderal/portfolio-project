from django.db import models
from datetime import datetime
class Blog(models.Model):
    title=models.CharField(max_length=255,blank=True)
    pub_date=models.DateTimeField(default=datetime.now(),blank=True)
    my_status=models.TextField()
    image=models.ImageField(upload_to= 'blog_images/')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.my_status[:100]

    def pub_date_simple(self):
        return self.pub_date.strftime('%b %e %Y')

    # Create your models here.
