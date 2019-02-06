from django.db import models

class Superadmin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.username
