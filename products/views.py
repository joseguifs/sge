from django.views import generic
from django.urls import reverse_lazy # resolve a url baseada no nome
from app.metrics import get_products_metrics 
from .models import Product
from .forms import ProductForm
from brands.models import Brand
from categories.models import Categorie
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer




class ProductList(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"
    paginate_by = 5
    permission_required = 'products.view_product'
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serial_number = self.request.GET.get('serial_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            queryset = queryset.filter(title__icontaisn = title)
        
        if serial_number:
            queryset.filter(serial_number__icontains = serial_number)
        
        if category:
            queryset = queryset.filter(category__icontains = category)
        
        if brand:
            queryset = queryset.filter(brand__id = brand)
        

        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['product_metrics'] = get_products_metrics()
        context['categories'] = Categorie.objects.all()
        context['brands'] = Brand.objects.all()
        return context

class ProductCreate(LoginRequiredMixin,PermissionRequiredMixin,generic.CreateView):
    model = Product
    template_name = "product_create.html"
    form_class = ProductForm
    success_url = reverse_lazy("product_list")
    permission_required = 'products.add_product'


class ProductDetailView(LoginRequiredMixin,PermissionRequiredMixin,generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
    permission_required = 'products.view_product'

class ProductUpdateView(LoginRequiredMixin,PermissionRequiredMixin,generic.UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    permission_required = 'products.change_product'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs = {'pk':self.object.id})
    

class   ProductDeleteView(LoginRequiredMixin,PermissionRequiredMixin,generic.DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer