from django.shortcuts import render, get_object_or_404
from .models import Pizza
from pizzas import models


# Create your views here.2
def index(request):
    """The home page for Pizzeria."""
    return render(request, "pizzas/index.html")


def pizzasName(request):
    pizzas = Pizza.objects.order_by("date_added")
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas_name.html", context)


def pizzaName(request, pizzaName_id):
    pizza = Pizza.objects.get(id=pizzaName_id)
    toppings = pizza.topping_set.order_by("-date_added")
    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/pizza_name.html", context)


def addPizza(request):
    if request.method == "POST":
        name = request.POST.get("name")
        obj = models.Pizza(name=name)
        obj.save()

    val = models.Pizza.objects.order_by("-date_added")
    return render(request, "pizzas/addPizza.html", {"pizzas": val})


def addTopping(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)

    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            models.Topping.objects.create(name=name, pizza=pizza)

    toppings = models.Topping.objects.filter(pizza=pizza).order_by("-date_added")
    return render(
        request, "pizzas/addToppings.html", {"pizza": pizza, "toppings": toppings}
    )
