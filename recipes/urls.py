from django.urls import path

from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<int:id>/', views.category, name="category"),
    path('single/<int:id>/', views.recipe, name="recipes"),
]
