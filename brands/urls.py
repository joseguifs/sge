from django.urls import path
from . import views


urlpatterns = [
    path('brand/list/',views.BrandList.as_view(), name = "brand_list"),
    path('brand/create/', views.BrandCreate.as_view(), name = "brand_create"),
    path('brand/<int:pk>/detail/',views.BrandDetailView.as_view(), name = "brand_detail"),
    path('brand/<int:pk>/update/', views.BrandUpdateView.as_view(), name = "brand_update"),
    path('brand/<int:pk>/delete/', views.BrandDeleteView.as_view(), name = "brand_delete"),
    path('api/v1/categories/', views.BrandListCreateApiView.as_view(), name = 'categorie-api'),
    path('api/v1/<int:pk>/categories/', views.BrandRetrieveUpdateDestroy.as_view(), name = 'categorie-api-gud'),
]