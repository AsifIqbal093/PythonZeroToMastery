"""Classes in Python."""

#Dog is the class
class Car:


    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'The {self.color} car has {self.mileage} miles.'

carA = Car('Blue', 20000)
carB = Car('Yellow', 30000)

print(carA)