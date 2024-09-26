from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import*
urlpatterns = [
    path('', product,name="product"),
    path('productdetails/<int:product_id>/', productdetails, name="productdetails")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)