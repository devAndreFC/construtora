from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('engineers/', views.engineer_list, name='engineers'),
    path('engineers/create/', views.engineer_create, name='engineer_create'),
    path('engineers/update/<int:id>/', views.engineer_update, name='engineer_update'),
    path('engineers/delete/<int:id>/', views.engineer_delete, name='engineer_delete'),

    path('materials/', views.material_list, name='materials'),
    path('materials/create/', views.material_create, name='material_create'),
    path('materials/update/<int:id>/', views.material_update, name='material_update'),
    path('materials/delete/<int:id>/', views.material_delete, name='material_delete'),

    path('projects/', views.project_list, name='projects'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/update/<int:project_id>/', views.project_update, name='project_update'),
    path('projects/delete/<int:id>/', views.project_delete, name='project_delete'),
]
