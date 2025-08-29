from django.db import models
from django.contrib.auth.models import User
# Create your models here. 

class Tag(models.Model):
    name=models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name
class Post(models.Model):
    post_tittle=models.CharField(max_length=60)
    post_content=models.TextField()
    post_date=models.DateField(auto_now=True) 
    tags=models.ManyToManyField(Tag,related_name='posts') 
    post_image=models.ImageField(upload_to='post/',default='post/1.png')

    def __str__(self):
        return self.post_tittle



class Comment(models.Model):
    comment=models.TextField()
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.comment




class Student(models.Model):
    name=models.CharField(max_length=50)
    stu_class=models.IntegerField()
    stu_age=models.IntegerField()
    