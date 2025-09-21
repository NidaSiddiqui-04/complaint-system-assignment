from django.db import models
from django.contrib.auth.models import User
from complaint_system import settings
# Create your models here.
class Complaint(models.Model):
    CATEGORY_CHOICES=(
        ('IT','IT Support'),
        ('Maintenance','Maintenance'),
        ('HR','HR'),
        ('Other','Other')
    )
    
    STATUS_CHOICES=(
        ('pending','Pending'),
        ('In Progress','In Progress'),
        ('Resolved','Resolved')
    )
    title=models.CharField(max_length=200)
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES ,max_length=20)
    status=models.CharField(choices=STATUS_CHOICES,default='Pending',max_length=25)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    attachment=models.FileField(upload_to='complaints/',null=True,blank=True,default='empty.jpg')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title