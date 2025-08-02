from django.db import models

class Brand(models.Model):
    name = models.CharField()
    description = models.TextField(max_length = 200, error_messages = {
        "max_length":"Comprimento exedido"
    }, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True) # campo é preenchido com o datetime local automaticamente 
    update_at = models.DateTimeField(auto_now = True) # mesma coisa do de cima porém pode ser editado e o de cima não

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name 