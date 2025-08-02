from django.urls import path
from . import views


urlpatterns = [
    path('outflow/list/',views.OutflowList.as_view(), name = "outflow_list"),
    path('outflow/create/', views.OutflowCreate.as_view(), name = "outflow_create"),
    path('outflow/<int:pk>/detail/',views.OutflowDetailView.as_view(), name = "outflow_detail"),
    path('api/v1/outflows/', views.OutflowListCreateApiView.as_view(), name = 'outflows_api'),
    path('api/v1/<int:pk>/outflows/', views.OutflowRetrieve.as_view(), name = 'outflows_api-gud'),
   
]