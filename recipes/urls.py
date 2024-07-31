# urls.py
from django.contrib import admin
from django.urls import path, include
# recipes/urls.py
from django.urls import path
from . import views

app_name = 'recipes'  # Ensure the app name is set for namespacing

urlpatterns = [
    path('', views.index, name='index'),
    path('service/<str:service_name>/', views.service_detail, name='service_detail'),
    # Add other paths as necessary
    path('admin/', admin.site.urls),
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

