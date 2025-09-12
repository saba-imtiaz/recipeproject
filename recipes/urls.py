from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # 👈 Homepage
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),

    # Auth
    path('accounts/login/', auth_views.LoginView.as_view(template_name='recipes/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # 👈 redirect to home
    path('signup/', views.signup_view, name='signup'),
]
