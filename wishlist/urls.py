from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='wishlist/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.my_wishlist, name='my_wishlist'),
    path('item/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('shared/<uuid:token>/', views.shared_wishlist, name='shared_wishlist'),
]
