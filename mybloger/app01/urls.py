from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'app01'

urlpatterns = [
    path('create_product/', views.create_product, name='upload_image'),
    path('image_list/', views.image_list, name='image_list'),
    path("01/", views.one,  name="index"),
    path("label/", views.label, name="label"),
    path("person/", views.person, name="person")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)