from django.urls import path
from . import views


urlpatterns = [
    path('supplier/list/',views.SupplierList.as_view(), name = "supplier_list"),
    path('supplier/create/', views.SupplierCreate.as_view(), name = "supplier_create"),
    path('supplier/<int:pk>/detail/',views.SupolierDetailView.as_view(), name = "supplier_detail"),
    path('supplier/<int:pk>/update/', views.SupplierUpdateView.as_view(), name = "supplier_update"),
    path('supplier/<int:pk>/delete/', views.SupolierDetailView.as_view(), name = "supplier_delete"),
    path('api/v1/suppliers/', views.SuppliersListCreateApiView.as_view(), name = 'supplier_delete_api'),
    path('api/v1/<int:pk>/suppliers/', views.SuppliersRetrieveUpdateDestroyAPIView.as_view(), name = 'supplier_api-gud'),
]