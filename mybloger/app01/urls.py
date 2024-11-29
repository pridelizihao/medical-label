from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_base64_image, image_list
from . import views

urlpatterns = [
    path('uploadBase64/', upload_base64_image, name='upload_image'),
    path('image_list/', image_list, name='image_list'),
    path("01/", views.one,  name="index")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)