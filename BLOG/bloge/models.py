from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=130)
    content=models.TextField()
    author=models.CharField(max_length=120)
    slug=models.CharField(max_length=130)
    timestamp=models.DateTimeField(blank=True)
    
    def __str__(self):
        return  self.title + 'by' + self.author
    


class Blogcomment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    posts=models.ForeignKey(post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    
    
    def __str__(self):
        return self.comment[0:13] +"...."+"by"+ self.user.first_name
     


