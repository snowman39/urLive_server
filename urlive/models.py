from django.db import models

class Room(models.Model):
	name = models.CharField(max_length=64,default='null')
	pincode = models.CharField(max_length=8, unique=True, default='null')
	
class User(models.Model):
	nickname= models.CharField(max_length=5, default='null')
	room = models.ForeignKey(Room, on_delete=models.CASCADE)

