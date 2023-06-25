from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('engineers/', views.list_engineer, name='engineers'),
    path('engineers/create/', views.create_engineer, name='create_engineer'),
    path('engineers/update/<int:id>/', views.update_engineer, name='update_engineer'),
    path('engineers/delete/<int:id>/', views.delete_engineer, name='delete_engeneer'),

    path('materials/', views.list_material, name='materials'),
    path('materials/create/', views.create_material, name='create_material'),
    path('materials/update/<int:id>/', views.update_material, name='update_material'),
    path('materials/delete/<int:id>/', views.delete_material, name='delete_material'),

]
