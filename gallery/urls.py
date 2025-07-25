
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home ,name='home'),
    path('Admin',views.admin_view,name='Admin'),
    path('art',views.art_view,name='art'),
    path('register',views.register_view ,name='register'),
    path('login',views.user_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('art/<int:pk>',views.buy_view,name='art'),
    path('list',views.list_buyed,name='list'),
    path('add-art',views.gallery_create,name='add_art')
]
