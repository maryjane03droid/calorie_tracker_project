from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    calories = models.PositiveIntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
