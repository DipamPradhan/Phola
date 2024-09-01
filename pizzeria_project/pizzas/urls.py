from django.urls import path
from . import views

app_name = "pizzas"

urlpatterns = [
    path("", views.index, name="index"),
    path("pizzasName/", views.pizzasName, name="pizzasName"),
    path("pizzasName/<int:pizzaName_id>/", views.pizzaName, name="pizzaName"),
    path("addPizza", views.addPizza, name="addPizza"),
    path("pizzasName/<int:pizza_id>/addTopping/", views.addTopping, name="addTopping"),
]
