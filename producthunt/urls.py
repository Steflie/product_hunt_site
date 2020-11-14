
from django.contrib import admin
from django.urls import path, include
from product_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('accounts/', include('account_app.urls')),
    path('products/', include('product_app.urls')),
]
