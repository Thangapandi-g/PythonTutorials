from Rectangle import Rectangle
from Customer import Customer
import pprint

rect1 = Rectangle(0,0, 100, 200)
rect2 = Rectangle(0,0, 300, 400)
rect3 = Rectangle(0,0, 600, 400)
#basic_ratio is a "class variable"
Rectangle.basic_ratio = 0.6
pprint.pprint(rect1.basic_ratio)
pprint.pprint(rect2.basic_ratio)
pprint.pprint(rect3.basic_ratio)

customer = Customer()
customer.name = "Alex"
pprint.pprint(customer.get_age())