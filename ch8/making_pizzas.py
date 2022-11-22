import pizza_module

pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza

make_pizza(16, 'pepperoni')

import pizza as p

p.make_pizza(16, 'pepperoni', 'shege')

from pizza import *

make_pizza(16, 'sapa')
