from django.shortcuts import render

from .models import Recipe

# Create your views here.


def home(request):
    recipes_all = Recipe.objects.filter(
        is_published=True
    )
    return render(request, 'recipes/pages/home.html', {
        'recipes': recipes_all,
    })


def category(request, id):
    recipes_category = Recipe.objects.filter(
        category__id=id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html', {
        'recipes': recipes_category,
    })


def recipe(request, id):
    recipe_single = Recipe.objects.filter(pk=id)
    return render(request, 'recipes/pages/single.html', {
        'recipes': recipe_single,
        'is_detail_page': True,
    })
