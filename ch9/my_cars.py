from car import Car, ElectricCar
#You import multiple classes by seperating them with a comma.

my_bettle = Car('volkswagen', 'beetle', 2019)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

#You can also import the entire module and access the classes via the modulename.Classname syntax


