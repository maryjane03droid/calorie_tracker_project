from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem
from .forms import FoodItemForm


def food_list(request):
    foods = FoodItem.objects.all().order_by('-date_added')
    total_calories = sum(food.calories for food in foods)

    return render(request, 'calorie_tracker/food_list.html', {
        'foods': foods,
        'total_calories': total_calories
    })


def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm()

    return render(request, 'calorie_tracker/add_food.html', {'form': form})


def edit_food(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)

    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm(instance=food)

    return render(request, 'calorie_tracker/edit_food.html', {'form': form})


def delete_food(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    food.delete()
    return redirect('food_list')


def reset_foods(request):
    FoodItem.objects.all().delete()
    return redirect('food_list')