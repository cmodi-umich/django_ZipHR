from django.test import TestCase
from .models import Airplane

class test_cases(TestCase):
    def test_immidiates_1(self):
        airplane = Airplane(plane_name="test", id=1, num_passengers=0)
        self.assertEqual(airplane.plane_name, "test")
        self.assertEqual(airplane.id, 1)
        self.assertEqual(airplane.num_passengers, 0)

    def test_immidiates_2(self):
        airplane = Airplane(plane_name="Chintan", id=100, num_passengers=101)
        self.assertEqual(airplane.plane_name, "Chintan")
        self.assertEqual(airplane.id, 100)
        self.assertEqual(airplane.num_passengers, 101)
    
    def test_immidiates_3(self):
        airplane = Airplane(plane_name="ZipAir", id=24, num_passengers=99)
        self.assertEqual(airplane.plane_name, "ZipAir")
        self.assertEqual(airplane.id, 24)
        self.assertEqual(airplane.num_passengers, 99)

    def test_fuel_1(self):
        airplane = Airplane(plane_name="ZipAir", id=5, num_passengers=0)
        self.assertEqual(airplane.fuel_capacity(), 1000)

    def test_fuel_2(self): # edge case where id is 0
        airplane = Airplane(plane_name="Chintan", id=0, num_passengers=101)
        self.assertEqual(airplane.fuel_capacity(), 0)
    
    def test_fuel_consumption_1(self): # whole number in log
        airplane = Airplane(plane_name="ZipAir", id=5, num_passengers=0)
        self.assertEqual(airplane.fuel_consumption(), 0.6021)

    def test_fuel_consumption_2(self): # decimal in log
        airplane = Airplane(plane_name="ZipAir", id=6, num_passengers=0)
        self.assertEqual(airplane.fuel_consumption(), 0.6812)

    def test_fuel_consumption_3(self): # adding in number of passengers
        airplane = Airplane(plane_name="ZipAir", id=5, num_passengers=5)
        self.assertNotEqual(airplane.fuel_consumption(), 0.6021) # make sure that we add number of passengers
        self.assertEqual(airplane.fuel_consumption(), 0.6031)

    def test_max_minutes_1(self):
        airplane = Airplane(plane_name="ZipAir", id=5, num_passengers=0)
        self.assertEqual(airplane.max_minutes(), 1660.8537)

    def test_max_minutes_2(self):
        airplane = Airplane(plane_name="ZipAir", id=5, num_passengers=5) # with passengers
        self.assertEqual(airplane.max_minutes(), 1658.0998)

    

