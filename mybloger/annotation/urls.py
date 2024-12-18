from django.urls import path
from. import views

urlpatterns = [
    path('coordinate_data/', views.coordinate_data, name='coordinate_data'),
    path('circlejsonndata/', views.circlejsonndata, name='circlejsonndata'),
    path('polygonjsonndata/', views.polygonjsonndata, name='polygonjsonndata'),
    path('label_list/', views.label_list, name='label_list'),
]