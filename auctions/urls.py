from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('listings/<int:pk>', views.listing_detail, name='listing'),
    path('categories', views.categories, name='categories'),
    path('categories/<int:category_id>', views.category_listings, name='category_listings'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('listings/create', views.listing_create, name='listing_create')
]
