from django.db import models
import numpy as np

class Airplane(models.Model):
    plane_name = models.CharField(max_length=50)
    id = models.PositiveIntegerField(primary_key=True)
    num_passengers = models.IntegerField()

    def fuel_capacity(self):
        return 200 * self.id

    def fuel_consumption(self):
        fuel_c_with_id = round(np.log10(round(self.id * 0.8, 4)), 4)
        fuel_c_of_pass = round(0.0002 * self.num_passengers, 4)
        return fuel_c_with_id + fuel_c_of_pass

    def max_minutes(self):
        fuel_cap = self.fuel_capacity()
        return round(fuel_cap / self.fuel_consumption(), 4)

    def __str__(self):
        name = "Summary for Plane: {}".format(self.plane_name)
        fuel = "Fuel Capacity: {}".format(self.fuel_capacity())
        fuel_consumption_ = "Fuel Consumption: {} liters per minute".format(self.fuel_consumption())
        max_mins = "Maximum Flying Time: {} minutes".format(self.max_minutes())
        return "{}\n{}\n{}\n{}".format(name, fuel, fuel_consumption_, max_mins)

    class Meta:
        ordering = ["id"]