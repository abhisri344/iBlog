from django.db import models
from datetime import datetime

# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,default='',help_text='Enter title of blog')
    head0=models.CharField(max_length=500,default='',help_text='Enter heading 0 for blog')
    chead0=models.TextField(max_length=5000,default='',help_text='Enter content for heading 0')
    head1=models.CharField(max_length=500,default='',help_text='Enter heading 1 for blog')
    chead1=models.TextField(max_length=5000,default='',help_text='Enter content for heading 1')
    head2=models.CharField(max_length=500,default='',help_text='Enter heading 2 for blog')
    chead2=models.TextField(max_length=5000,default='',help_text='Enter content for heading 2')
    pub_date=models.DateField(default=datetime.now,blank=True)
    author=models.CharField(max_length=24,default='',help_text='Enter your name')
    thumbnail=models.ImageField(upload_to='blog/media',default='')
    
    def __str__(self):
        return self.title
    
