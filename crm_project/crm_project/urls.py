from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
    path('customers/', include('customers.urls', namespace='customers')),
    path('suppliers/', include('suppliers.urls', namespace='suppliers')),
    path('dashboard/', include('core.urls')),
    path('', RedirectView.as_view(url='/dashboard/', permanent=True), name='index'),
]
