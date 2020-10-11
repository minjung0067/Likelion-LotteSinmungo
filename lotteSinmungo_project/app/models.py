from django.db import models

class Problem (models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True) 

class Problem_solutions(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    original_date = models.DateTimeField(auto_now=False)
    upload_date = models.DateTimeField(auto_now=True)