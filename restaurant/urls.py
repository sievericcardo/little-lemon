from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),

    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),

    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),

    path('categories', views.categories_view, name="categories"),
    path('categories/<int:pk>', views.single_category_view, name="single_category"),

    path('orders', views.order_view, name="orders"),
    path('orders/<int:pk>', views.single_order_view, name="single_order"),

    path('bookings', views.bookings, name="bookings"), 

    path('login', views.login_view, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register', views.signup, name="register"),
    path('profile', views.user_profile, name="user_profile"),
    path('api-token-auth', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]