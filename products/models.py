from django.db import models
from categories.models import Categorie
from brands.models import Brand

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 200)
    category = models.ForeignKey(Categorie, on_delete = models.PROTECT, related_name = "procuct_category")
    brand = models.ForeignKey(Brand, on_delete = models.PROTECT, related_name = "product_brand")
    description = models.TextField(blank = True, null = True)
    serial_number = models.CharField(max_length = 100, null = True, blank = True)
    cost_price = models.DecimalField(max_digits = 19, decimal_places = 4)
    selling_price = models.DecimalField(max_digits = 19, decimal_places = 4)
    quantity = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True) # campo é preenchido com o datetime local automaticamente 
    update_at = models.DateTimeField(auto_now = True) # mesma coisa do de cima porém pode ser editado e o de cima não

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title