from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Users(auth.models.User):

    def __str__(self):
        return self.username

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)




class Category (models.Model):
    name = models.CharField(max_length=80 )

    def __str__(self):
        return self.name



class Subscribe(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subscriber_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{} subscribe to {}'.format(self.subscriber_id, self.category_id)
    class Meta:
        unique_together = ["category_id", "subscriber_id"]
            
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    # image= models.ImageField(upload_to='images', null=True)
    image= models.ImageField(verbose_name="image",upload_to='images/', null=True, )
    cat=models.ForeignKey(Category,null=True,on_delete= models.CASCADE)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    # email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, default=1)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Reply (models.Model):
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='replies')
    author = models.ForeignKey(User, on_delete= models.CASCADE, default=1)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Reply {} by {}'.format(self.body, self.name)


class Likes(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    isLiked=models.BooleanField(null=True)

