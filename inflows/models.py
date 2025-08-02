from django.db import models
from suppliers.models import Suppliers
from products.models import Product

# Create your models here.
class Inflow(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete = models.PROTECT, related_name = "inflow_suppliers")
    product = models.ForeignKey(Product, on_delete = models.PROTECT, related_name = "inflow_product")
    quantity = models.IntegerField()
    description = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True) # campo é preenchido com o datetime local automaticamente 
    update_at = models.DateTimeField(auto_now = True) # mesma coisa do de cima porém pode ser editado e o de cima não

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return str(self.product)