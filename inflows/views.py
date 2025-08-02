from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy # resolve a url baseada no nome 
from .models import Inflow
from .forms import InflowForm
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from rest_framework import generics
from .models import Inflow
from .serializers import InflowSerializer



class InflowList(LoginRequiredMixin,generic.ListView):
    model = Inflow
    template_name = "inflow_list.html"
    context_object_name = "inflows"
    paginate_by = 5
    permission_required = 'inflows.view_inflow'
    
    
    def get_queryset(self):
        queryset = super().get_queryset() if not self.request.GET.get("product") else self.model.objects.filter(product__title__icontains = self.request.GET.get("product"))
        
        return queryset


class InflowCreate(LoginRequiredMixin,PermissionRequiredMixin,generic.CreateView):
    model = Inflow
    template_name = "inflow_create.html"
    form_class = InflowForm
    success_url = reverse_lazy("inflow_list")
    permission_required = 'inflows.add_inflow'

class InflowDetailView(LoginRequiredMixin,PermissionRequiredMixin,generic.DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'

class InflowListCreateApiView(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer
    

class InflowRetrieveUpdateDestroy(generics.RetrieveUpdateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer