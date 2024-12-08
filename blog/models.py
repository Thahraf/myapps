from django.db import models
from django.utils.text import slugify
# Create your models here.
# category
class Category(models.Model):
    name = models.CharField(null=True,max_length=200)
    
    def __str__(self): 
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=200,null = True)
    content = models.TextField(null=True)
    img_url = models.URLField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
    content = models.TextField()    
 
        
    