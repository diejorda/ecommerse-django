from django.urls import path


from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('shirt', views.shirt, name='shirt'),
    path('sw',views.sw, name='sw'),
    path('ow', views.ow, name='ow'),
    path('search', views.search, name='search'),
]

