from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
# from django.contrib.auth import login, logout
from blog.models import User
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from blog.forms import UserForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from blog.forms import UserForm
from django.views.generic import CreateView


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserForm
    # success_url = reverse_lazy('login') #reverse_lazy to redirect the user to the login page upon successful registration.
    template_name = 'html/signup.html'
    # return httpResponseRedirect(success_url)

    def signup(request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()

                user.save()

                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return HttpResponseRedirect("login")
        else:
            form = UserForm()
            return render(request, 'html/signup.html', {'form': form})
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404





# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
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
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})



# def home(request):
#     return render(request, 'index.html')


# def register(request):
#     if request.method == "POST":
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect("/blog/home")
#     else:
#         user_form= UserForm()
#         context= {'user_form': user_form}
#         return render(request, 'register.html', context)


