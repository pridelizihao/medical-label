from django.urls import path
from. import views

app_name = 'annotation'

urlpatterns = [
    path('rectjsondata/<int:image_id>/<int:type>', views.rectjsondata, name='rectjsondata'),
    path('circlejsondata/<int:image_id>/<int:type>', views.circlejsonndata, name='circlejsondata'),
    path('polygonjsondata/<int:image_id>/<int:type>', views.polygonjsonndata, name='polygonjsondata'),
    path("penciljsondata/<int:image_id>/<int:type>", views.penciljsondata, name="penciljsondata"),
    path('saveimage/<int:image_id>', views.saveimage, name='saveimage'),
    path('label_list/', views.label_list, name='label_list'),
    path('labeledshow/', views.labeledshow, name='labeledshow'),
]