from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create_product', views.create_product, name='upload_image'),
    path('image_list', views.image_list, name='image_list'),
    path("01", views.one,  name="index")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)