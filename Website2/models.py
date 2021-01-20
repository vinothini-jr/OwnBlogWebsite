from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return str(self.name)

class PostPage(models.Model):
    category=models.ForeignKey(Category,related_name="posts",on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    content=RichTextUploadingField(blank=True,null=True)
    slug=models.SlugField(unique=True,null=True)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    seo_des=models.CharField(max_length=200,null=True)
    seo_keywords = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail',kwargs={"slug":str(self.slug)})
class Home(models.Model):
    images=models.ImageField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return str(self.images)
class Comment(models.Model):
    post=models.ForeignKey(PostPage,related_name="comments",on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200)
    mail=models.EmailField()
    body=models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    msg=models.TextField()

    def __str__(self):
        return self.name



