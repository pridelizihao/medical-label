from django.urls import path
from. import views

app_name = 'annotation'

urlpatterns = [
    path('rectjsondata/<int:image_id>/<int:type>', views.rectjsondata, name='rectjsondata'),
    path('circlejsondata/', views.circlejsonndata, name='circlejsondata'),
    path('polygonjsondata/', views.polygonjsonndata, name='polygonjsondata'),
    path("penciljsondata/", views.penciljsondata, name="penciljsondata"),
    path('label_list/', views.label_list, name='label_list'),
]