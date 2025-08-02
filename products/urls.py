from django.urls import path
from . import views


urlpatterns = [
    path('product/list/',views.ProductList.as_view(), name = "product_list"),
    path('product/create/', views.ProductCreate.as_view(), name = "product_create"),
    path('product/<int:pk>/detail/',views.ProductDetailView.as_view(), name = "product_detail"),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name = "product_update"),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name = "product_delete"),
    path('api/v1/products/', views.ProductListCreateApiView.as_view(), name = 'products_api'),
    path('api/v1/<int:pk>/products/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name = 'products_api-gud'),
]