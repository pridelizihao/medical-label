from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = 'app01'

urlpatterns = [
    path('upload_image/', views.create_product, name='upload_image'),
    path('image_list/', views.image_list, name='image_list'),
    path("label/", views.label, name="label"),
    path("person/", views.person, name="person"),
    path("edit_profile/",views.edit_profile, name="edit_profile"),
    path("profile/",views.profile, name="profile"),
    path("home/",views.home, name="home"),
    path("upload_product2/",views.upload_folder, name="upload_product2"),
    path("delete_image/<int:image_id>/",views.delete_image, name="delete_image"),
    path("image_is_labeled/",views.image_labeled, name="image_is_labeled"),
    path("image_is_ailabeled/",views.image_ailabeled, name="image_is_ailabeled"),
    path("annotate_image/<int:image_id>/",views.annotate_image, name="annotate_image"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)