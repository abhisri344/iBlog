from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
import random
from django.views.generic import View
from django.shortcuts import redirect
from .forms import Addblog
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'blog/base.html')
def blogs(request):
    p=Blogpost.objects.all()
    return render(request,'blog/blogs.html',{'mypost':p})
def blogpost(request,id):
    post=Blogpost.objects.filter(post_id=id)[0]
    return render(request,'blog/blogpost.html',{'posts':post})        
def home(request):
    p=Blogpost.objects.all()
    # print(len(p))
    randomNum = random.randint(0, len(p)-1)
    p=Blogpost.objects.all()[randomNum]
    # print(p)
    return render(request,'blog/home.html',{'mypost':p})   
class AddBlog(View):
    def get(self,request):
        form=Addblog(None)
        return render(request,'blog/addblog.html',{'f':form})
    def post(self,request):
        form=Addblog(request.POST,request.FILES) 
        form.save()
        return redirect('/blogs')         
def search(request):
    query=request.GET.get('search')
    if query:
        match=Blogpost.objects.filter(Q(title__contains=query)|Q(head0__contains=query)|Q(head1__contains=query)|Q(head2__contains=query))
        #title__contains=query,head0__contains=query,head1__contains=query,head2__contains=query  Q()|
        return render(request,'blog/blogs.html',{'mypost':match})