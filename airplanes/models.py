from django.db import models
import numpy as np


class Airplane(models.Model):
    '''
    Model for airplane
    Fields include, plane name, id and number of passengers
    '''
    plane_name = models.CharField(max_length=50)
    id = models.PositiveIntegerField(primary_key=True)
    num_passengers = models.IntegerField()

    def fuel_capacity(self):
        '''
        Calculate fuel capacity by multiplying id by 200 liters
        '''
        return 200 * self.id

    def fuel_consumption(self):
        '''
        Find fuel consumption that comes from id by taking the log base 10 of the id multiplied by 0.8
        Find fuel onsumption per passenger by multiplying 0.0002 by each passenger
        Return sum of both
        '''
        fuel_c_with_id = round(np.log10(round(self.id * 0.8, 4)), 4)
        fuel_c_of_pass = round(0.0002 * self.num_passengers, 4)
        return fuel_c_with_id + fuel_c_of_pass

    def max_minutes(self):
        '''
        Return fuel capacity divided by fuel consumption to see the maximum number of minutes the plane can fly
        '''
        fuel_cap = self.fuel_capacity()
        return round(fuel_cap / self.fuel_consumption(), 4)

    def __str__(self):
        '''
        String summary of the airplane model
        '''
        name = "Summary for Plane: {}".format(self.plane_name)
        fuel = "Fuel Capacity: {}".format(self.fuel_capacity())
        fuel_consumption_ = "Fuel Consumption: {} liters per minute".format(self.fuel_consumption())
        max_mins = "Maximum Flying Time: {} minutes".format(self.max_minutes())
        return "{}\n{}\n{}\n{}".format(name, fuel, fuel_consumption_, max_mins)

    class Meta:
        '''
        Done to order the planes by id when they are presented 
        '''
        ordering = ["id"]