from django.contrib import admin
from django.urls import path, include
from recipes import views
# foodbites/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),  # Include the recipes app URLs
    path('', views.index, name='index'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('submit/', views.submit_recipe, name='submit_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('accounts/profile/', views.user_dashboard, name='user_dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]
