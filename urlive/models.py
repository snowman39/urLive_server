from django.db import models

class Room(models.Model):
	name = models.CharField(max_length=64, default='null')
	pincode = models.CharField(max_length=8, unique=True, default='null')
	encrypt= models.CharField(max_length= 20, unique=True, default='null')
	
class User(models.Model):
	nickname= models.CharField(max_length=5, default='null')
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	uid = models.TextField()

class Memo(models.Model):
	url = models.TextField()
	content= models.TextField()
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	author = models.CharField(max_length=5, default='null')
	

