from django.urls import path
from . import views

urlpatterns = [
    path('',views.patient_list,name="patient_list"),
    path('create/',views.patient_created,name="patient_created"),
    path('<int:pk>/update/', views.patient_update, name='patient_update'),
    path('<int:pk>/delete/', views.patient_delete, name='patient_delete'),
]
