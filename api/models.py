from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=False, null=False)

    """
    Created a sales opportunity based on
    the count of vehicles
    return: bool
    """
    @property
    def sales_opportunity(self):
        return self.vehicles.count() == 0

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    COLORS_CHOICES = [
        ("yellow", "yellow"),
        ("blue", "blue"),
        ("gray", "gray"),
    ]

    MODELS_CHOICES = [
        ("hatch", "hatch"),
        ("sedan", "sedan"),
        ("convertible", "convertible"),
    ]

    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, related_name="vehicles", on_delete=models.CASCADE, blank=False, null=False)
    color = models.CharField(max_length=20, choices=COLORS_CHOICES, blank=False, null=False)
    model = models.CharField(max_length=20, choices=MODELS_CHOICES, blank=False, null=False)

    def __str__(self):
        return f"{self.color} - {self.model}"
