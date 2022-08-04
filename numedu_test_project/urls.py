from django.contrib import admin
from django.urls import path, include
from storage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('deleteitem/<int:pk>/', views.delete_item),
    path('add_staff/', views.add_staff, name='staff'),
    path('add_storage/', views.add_storage, name='storage'),
    path('delete_storage/<int:pk>/', views.delete_storage, name='del_store'),
    path('add_machine/', views.add_machine, name='machine'),
    path('one_storage/<int:pk>/', views.one_storage, name='one')
]
