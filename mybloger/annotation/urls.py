from django.urls import path
from. import views

app_name = 'annotation'

urlpatterns = [
    path('rectjsondata/', views.coordinate_data, name='rectjsondata'),
    path('circlejsonndata/', views.circlejsonndata, name='circlejsonndata'),
    path('polygonjsonndata/', views.polygonjsonndata, name='polygonjsonndata'),
    path("penciljsondata/", views.penciljsondata, name="penciljsondata"),
    path('label_list/', views.label_list, name='label_list'),
]