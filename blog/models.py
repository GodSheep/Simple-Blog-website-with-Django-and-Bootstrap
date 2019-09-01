from django.db import models
from django.contrib.auth.models import User

from mdeditor.fields import MDTextField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

allcategory = (
        ('life', u'生活'),
        ('study', u'学习'),
        ('stuff', u'碎念'),
        ('aboutme', u'关于'),
)



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    Category = models.CharField(max_length=50,blank=True,
                              choices=allcategory)
    Tag = models.CharField(max_length = 50, blank = True)  #博客标签

    #content = models.TextField()
    content = MDTextField('content')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

