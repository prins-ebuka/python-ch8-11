import car
#importing an entire module
#here to access the classes, we use the modulename.Classname syntax

my_bettle = car.Car('volkswagen', 'beetle', 2019)
print(my_bettle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
