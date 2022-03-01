from django.urls import path
from pyrsistent import v
from . import views

urlpatterns = [
    path('', views.index, name="dashboard-index"),
    path('staff/', views.staff, name='dashboard-staff'),
    path('porduct/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order'),
]
