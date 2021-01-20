
from django.shortcuts import render,redirect,HttpResponse
from.models import PostPage, Category,Contact, Home
from .forms import CommentForm

# Create your views here.
def HomePage(request):
    posts=PostPage.objects.all()
    pic=Home.objects.all()
    context={
        "posts":posts,
        "pic":pic
    }
    return render(request,'Website2/homeHtml.html',context)

def DetailPage(request,slug):
    post = PostPage.objects.get(slug=slug)
    form = CommentForm()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            obj=form.save()
            obj.post = post
            obj.save()
            return redirect("detail",slug=slug)
    context={
        "post":post,
        "form":form
    }
    return render(request,'Website2/detailHtml.html',context)

def category(request,slug):
    category = Category.objects.get(slug=slug)
    context={
        "category":category
    }
    return render(request,'Website2/categoryHtml.html',context)
def about(request):
    return render(request, 'Website2/aboutHtml.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name",'')
        email=request.POST.get("email",'')
        msg=request.POST.get("msg",'')
        contact=Contact(name=name,email=email,msg=msg)
        contact.save()
    return render(request, 'Website2/contactHtml.html')