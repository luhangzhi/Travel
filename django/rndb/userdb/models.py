from django.db import models
#coding:utf-8
# Create your models here.
class Users(models.Model):
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	nickname=models.CharField(max_length=50)
	introduce=models.CharField(max_length=100)
	sex=models.CharField(max_length=10)
	#head=ImageField("/home/zhangyongde/Desktop/django/picture")
	city=models.CharField(max_length=50)
	def __unicode__(self):
		return self.username
