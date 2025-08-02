from django.db import models

# Create your models here.
class Suppliers(models.Model):
    name = models.CharField()
    description = models.TextField(max_length = 200, error_messages = {
        "max_length":"Comprimento exedido"
    }, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True) 
    update_at = models.DateTimeField(auto_now = True) 

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name 