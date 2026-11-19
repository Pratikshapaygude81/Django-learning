from django.urls import path
from . import views
urlpatterns = [
    path('',views.ProviderAPIView.as_view(),name='provider')
]
