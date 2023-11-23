from importlib.resources import path
from django.urls import path
from eruna import views

app_name = 'eruna'

urlpatterns = [
    path('', views.DestinationListView.as_view(), name='home'),
    path('destinations/', views.DestinationListView.as_view(), name='destinations'),
    path('destinations/<str:slug>', views.DestinationDetialView.as_view(), name='destination-detail'),
    path('sessiontest/', views.TestSecurityView.as_view(), name='test-session')
]