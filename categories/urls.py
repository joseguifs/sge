from django.urls import path
from . import views


urlpatterns = [
    path('categorie/list/',views.CategorieList.as_view(), name = "categorie_list"),
    path('categorie/create/', views.CategorieCreate.as_view(), name = "categorie_create"),
    path('categorie/<int:pk>/detail/',views.CategorieDetailView.as_view(), name = "categorie_detail"),
    path('categorie/<int:pk>/update/', views.CategorieUpdateView.as_view(), name = "categorie_update"),
    path('categorie/<int:pk>/delete/', views.CategorieDeleteView.as_view(), name = "categorie_delete"),
    path('api/v1/categories/', views.CategorieListCreateApiView.as_view(), name = 'categorie-api'),
    path('api/v1/<int:pk>/brands/', views.CategorieRetrieveUpdateDestroy.as_view(), name = 'categorie-api-gud')
]