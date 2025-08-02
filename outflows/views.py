from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy # resolve a url baseada no nome 
from .models import Outflows
from .forms import OutflowForm
from app.metrics import get_sales_metrics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics
from .models import Outflows
from .serializers import OutflowSerializer



class OutflowList(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    model = Outflows
    template_name = "outflow_list.html"
    context_object_name = "outflows"
    paginate_by = 5
    permission_required = 'outflows.view_outflows'
    
    
    def get_queryset(self):
        queryset = super().get_queryset() if not self.request.GET.get("product") else self.model.objects.filter(product__title__icontains = self.request.GET.get("product"))
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['sales_metric'] = get_sales_metrics()
        return context


class OutflowCreate(LoginRequiredMixin,PermissionRequiredMixin,generic.CreateView):
    model = Outflows
    template_name = "outflow_create.html"
    form_class = OutflowForm
    success_url = reverse_lazy("outflow_list")
    permission_required = 'outflows.add_outflows'


class OutflowDetailView(LoginRequiredMixin,PermissionRequiredMixin,generic.DetailView):
    model = Outflows
    template_name = 'outflow_detail.html'
    permission_required = 'outflows.view_outflows'


class OutflowListCreateApiView(generics.ListCreateAPIView):
    queryset = Outflows.objects.all()
    serializer_class = OutflowSerializer
    

class OutflowRetrieve(generics.RetrieveAPIView):
    queryset = Outflows.objects.all()
    serializer_class = OutflowSerializer