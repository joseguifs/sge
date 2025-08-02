from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy # resolve a url baseada no nome 
from .models import Suppliers
from .forms import SupplierForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from rest_framework import generics
from .models import Suppliers
from .serializers import SuppliersSerializer


class SupplierList(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    model = Suppliers
    template_name = "supplier_list.html"
    context_object_name = "suppliers"
    paginate_by = 5
    permission_required = 'suppliers.view_supplier'

    
    def get_queryset(self):
        queryset = super().get_queryset() if not self.request.GET.get("name") else self.model.objects.filter(name__icontains = self.request.GET.get("name"))
        
        return queryset


class SupplierCreate(LoginRequiredMixin,PermissionRequiredMixin,generic.CreateView):
    model = Suppliers
    template_name = "supplier_create.html"
    form_class = SupplierForm
    success_url = reverse_lazy("supplier_list")
    permission_required = 'suppliers.add_supplier'


class SupolierDetailView(LoginRequiredMixin,PermissionRequiredMixin,generic.DetailView):
    model = Suppliers
    template_name = 'supplier_detail.html'
    permission_required = 'suppliers.view_supplier'



class SupplierUpdateView(LoginRequiredMixin,PermissionRequiredMixin,generic.UpdateView):
    model = Suppliers
    template_name = 'supplier_update.html'
    form_class = SupplierForm
    permission_required = 'suppliers.change_supplier'

    def get_success_url(self):
        return reverse_lazy('supplier_detail', kwargs = {'pk':self.object.id})
    

class SupplierDeleteView(LoginRequiredMixin,PermissionRequiredMixin,generic.DeleteView):
    model = Suppliers
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
    permission_required = 'suppliers.delete_supplier'


class SuppliersListCreateApiView(generics.ListCreateAPIView):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    

class SuppliersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer