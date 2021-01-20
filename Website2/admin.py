from django.contrib import admin
from .models import PostPage, Category, Comment, Contact,Home

# Register your models here.
admin.site.register(PostPage)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Home)
