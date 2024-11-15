from django.db import models

# Create your models here.

class Friend(models.Model):
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10)
    
    def _str_(self):
        return self.name