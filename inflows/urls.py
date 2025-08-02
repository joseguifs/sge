from django.urls import path
from . import views


urlpatterns = [
    path('inflow/list/',views.InflowList.as_view(), name = "inflow_list"),
    path('inflow/create/', views.InflowCreate.as_view(), name = "inflow_create"),
    path('inflow/<int:pk>/detail/',views.InflowDetailView.as_view(), name = "inflow_detail"),
    path('api/v1/inflows/', views.InflowListCreateApiView.as_view(), name = 'inflow_api'),
    path('api/v1/<int:pk>/inflows/', views.InflowRetrieveUpdateDestroy.as_view(), name = 'inflow_api-gud'),
]
