from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('sge/',views.home, name = "home"),
    path('logout', auth_views.LogoutView.as_view(), name = 'logout'),
    path('sge/',include('brands.urls')),
    path('sge/', include('categories.urls')),
    path('sge/', include('suppliers.urls')),
    path('sge/', include("inflows.urls")),
    path('sge/', include('outflows.urls')),
    path('sge/', include('products.urls')),
    path('sge/', include('authentication.urls')),

]
