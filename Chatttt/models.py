from django.db import models

class Friend(models.Model):
    username= models.CharField(max_length=100)
    friends = models.TextField()

class Messages(models.Model):
    key = models.CharField(max_length =100)
    sender = models.CharField(max_length = 100)
    receiver = models.CharField(max_length = 100)
    message = models.TextField()
    timestamp = models.TimeField()

        
    
