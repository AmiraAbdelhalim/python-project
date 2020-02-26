from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from blog.models import Users
from blog.models import Users , Reply
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from blog.forms import UserForm
from django.views.generic import CreateView
from django.views import generic
from .models import Post , Comment ,Subscribe,Category
from .forms import CommentForm , ReplyForm , PostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.text import slugify
#from django.contrib.auth.forms import AuthenticationForm
from .models import Post 
from .forms import CommentForm , ReplyForm







class SignUp(CreateView):
    form_class = forms.UserForm
    success_url = reverse_lazy('login')
    # #reverse_lazy to redirect the user to the login page upon successful registration.
    template_name = 'signup.html'

def home(request):
    return render(request, 'index.html')




# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'
#     paginate_by = 3

def PostList(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    cats = Category.objects.all()
    subs = Subscribe.objects.filter(subscriber_id=request.user).values_list('category_id', flat=True)
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    check = checks(cats,subs)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'index.html',
                  {'page': page,
                   'post_list': post_list,
                   'cats': cats,
                   'checks': check})




def post_detail(request, slug):
    url = '/blog/' + slug
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    replies = Reply.objects.all()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            # return HttpResponseRedirect(url)
    else:
        comment_form = CommentForm()
        reply_form = ReplyForm()
        

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'reply_form':ReplyForm,
                                           'replies': replies})


def comment_reply(request,commentId,slug):
    comment = get_object_or_404(Comment,id=commentId)
    print(comment)
    url = '/blog/'+slug

    if request.method =='POST':
        print(request.GET)
        reply_form = ReplyForm(data=request.POST)
        print(reply_form)
        if reply_form.is_valid():

            reply = reply_form.save(commit=False)

            reply.comment = comment
            reply.name = request.user

            reply.save()

    else:
        reply_form = ReplyForm()

    return HttpResponseRedirect(url)


def newPost(request):
    template_name = 'newPost.html'

    # new_form = None
    if request.method=="POST":
        form = PostForm(request.POST,request.FILES)
        if(form.is_valid()):
            print("vaild")
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.slug=slugify(new_form.title)
            new_form.save()
            # form.save()
            return HttpResponseRedirect('/blog')
    else:
        form = PostForm()
  

    context = {
            'form' : form,
            }

    return render (request,template_name,context)


def listCat(request,catid):
    post=Post.models.filter(cat_id=catid)
    if request.method =='POST':
        form = PostForm(data=request.POST)
        
        if form.is_valid():

            form.save()

    else:
        form = PostForm()

    return HttpResponseRedirect(url)




def subscribe(request, category_id):
    try:
        cat = Category.objects.get(id = category_id)
        Subscribe.objects.create(subscriber_id = request.user, category_id = cat)
    finally:
        return HttpResponseRedirect('/blog')


def unsubscribe(request,category_id):
    try:
        cat = Category.objects.get(id = category_id)
        sub = Subscribe.objects.get(subscriber_id = request.user, category_id = cat)
        sub.delete()
    finally:
        return HttpResponseRedirect('/blog')


def checks (cats,subs):
    checks= []
    for cat in cats:
        if cat.id in subs:
            check = cat.id

        else:
            check =-1
        checks.append(check)

    return checks



def PostList(request):
    all_posts = Post.objects.all()
    context = {'post' : all_posts}
    return render(request ,'home.html' , context)
