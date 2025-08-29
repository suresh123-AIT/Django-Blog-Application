from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse 
from .models import Post,Tag
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator 
from .forms import CommentForm 
from django.urls import reverse 
from django.db.models import Q

posts=[
    {
        'id':1,
        'tittle':'cricket is the big game',
        'content':'India won the t20 world cup 2024',
    },
    {
        'id':2,
        'tittle':'war should be avoided',
        'content':'India attacks pakistan because of terror activity',
    },
    {
        'id':3,
        'tittle':'Movie is for entertainment',
        'content':'kubera is movie of Dhanush which runs around money',
    },
]
# Create your views here. 
def home(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/accounts/login/') 
    # else:
    all_post=Post.objects.all().order_by('-id')
    paginator=Paginator(all_post,4)
    page_number=request.GET.get('p',1) 
    paginator_obj=paginator.get_page(page_number)
    return render(request,'posts/index.html',{'posts':paginator_obj,'total':all_post.count()}) 
def post(request,id):
    post=get_object_or_404(Post,id=id)
    if(request.method=="POST"):
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post 
            comment.user=request.user
            comment.save()
            posturl=reverse('post',args=[id])
            return HttpResponseRedirect(posturl)

    else:
        form=CommentForm()
    return render(request,'posts/post.html',{'post_dict':post,'form':form,'comments':post.comment_set.all( )})  

def Tags(request,id):
    tag=Tag.objects.get(id=id)
    return render(request,'posts/tags.html',{'tags':tag.posts.all()}) 

def search(request):
    query=request.GET.get('query','')
    page_number=request.GET.get('p',1)
    posts=Post.objects.filter(Q(post_tittle__icontains=query) | Q(post_content__icontains=query)).order_by('-id') 
    paginator=Paginator(posts,4)
    page_obj=paginator.get_page(page_number)
    return render(request,'posts/search.html',{'posts':page_obj,'query':query,'total':posts.count()})