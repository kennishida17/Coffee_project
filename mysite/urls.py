from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('top/', views.index, name='index'),
    path('overview/', views.overview, name='overview'),
    path('contact/', views.contact, name='contact'),
    path('add/', views.add, name='add'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('admin/', admin.site.urls)
]
