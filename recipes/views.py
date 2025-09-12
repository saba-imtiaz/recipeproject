from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe, Category, Comment
from django.contrib.auth.decorators import login_required

def recipe_list(request):
    category_id = request.GET.get("category")
    search_query = request.GET.get("search")

    recipes = Recipe.objects.all()

    if category_id:
        recipes = recipes.filter(category_id=category_id)
    if search_query:
        recipes = recipes.filter(title__icontains=search_query) | recipes.filter(ingredients__icontains=search_query)

    categories = Category.objects.all()
    return render(request, "recipes/recipe_list.html", {"recipes": recipes, "categories": categories})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST" and request.user.is_authenticated:
        Comment.objects.create(
            recipe=recipe,
            author=request.user,
            text=request.POST["text"]
        )
        return redirect("recipe_detail", pk=pk)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})

@login_required
def add_recipe(request):
    categories = Category.objects.all()
    if request.method == "POST":
        Recipe.objects.create(
            title=request.POST["title"],
            ingredients=request.POST["ingredients"],
            instructions=request.POST["instructions"],
            image=request.FILES.get("image"),
            author=request.user,
            category_id=request.POST["category"]
        )
        return redirect("recipe_list")
    return render(request, "recipes/add_recipe.html", {"categories": categories})

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("recipe_list")
    else:
        form = UserCreationForm()
    return render(request, "recipes/signup.html", {"form": form})
def home(request):
    return render(request, "recipes/home.html")
