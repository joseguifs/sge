
from django.views import generic
from django.urls import reverse_lazy # resolve a url baseada no nome 
from .models import Categorie
from .forms import CategorieForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics
from .models import Categorie
from serializers import CategorieSerializer



class CategorieList(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    model = Categorie
    template_name = "categorie_list.html"
    context_object_name = "categories"
    paginate_by = 5
    permission_required = 'categories.view_categorie'
    
    def get_queryset(self):
        queryset = super().get_queryset() if not self.request.GET.get("name") else self.model.objects.filter(name__icontains = self.request.GET.get("name"))
        
        return queryset


class CategorieCreate(LoginRequiredMixin,PermissionRequiredMixin,generic.CreateView):
    model = Categorie
    template_name = "categorie_create.html"
    form_class = CategorieForm
    success_url = reverse_lazy("categorie_list")
    permission_required = 'categories.add_categorie'

class CategorieUpdateView(generic.UpdateView):
    model = Categorie
    template_name = 'categorie_update.html'
    form_class = CategorieForm
    permission_required = 'categories.change_categorie'

    def get_success_url(self):
        return reverse_lazy('categorie_detail', kwargs = {'pk':self.object.id})


class CategorieDetailView(LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    model = Categorie
    template_name = 'brand_detail.html'
    permission_required = 'categories.view_categorie'


class CategorieDeleteView(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    model = Categorie
    template_name = 'categorie_delete.html'
    success_url = reverse_lazy('categorie_list')
    permission_required = 'categories.delete_categorie'



class BrandListCreateApiView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    

class BrandRetrieveUpdateDestroy(generics.RetrieveUpdateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer