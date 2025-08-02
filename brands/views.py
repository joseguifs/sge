from django.views import generic
from django.urls import reverse_lazy # resolve a url baseada no nome 
from .models import Brand
from .forms import BrandForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics
from .serializer import BrandSerializer


class BrandList(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    model = Brand
    template_name = "brand_list.html"
    context_object_name = "brands"
    paginate_by = 5
    permission_required = 'brands.view_brand'
    
    def get_queryset(self):
        queryset = super().get_queryset() if not self.request.GET.get("name") else self.model.objects.filter(name__icontains = self.request.GET.get("name"))
        
        return queryset


class BrandCreate(LoginRequiredMixin,PermissionRequiredMixin,generic.CreateView):
    model = Brand
    template_name = "brand_create.html"
    form_class = BrandForm
    success_url = reverse_lazy("brand_list")
    permission_required = 'brands.add_brand'


class BrandDetailView(LoginRequiredMixin,PermissionRequiredMixin,generic.DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    permission_required = 'categories.view_categorie'

class BrandUpdateView(LoginRequiredMixin,PermissionRequiredMixin,generic.UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    permission_required = 'brands.change_brand'

    def get_success_url(self):
        return reverse_lazy('brand_detail', kwargs = {'pk':self.object.id})
    

class BrandDeleteView(LoginRequiredMixin,PermissionRequiredMixin,generic.DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.delete_brand'

class BrandListCreateApiView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    

class BrandRetrieveUpdateDestroy(generics.RetrieveUpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
