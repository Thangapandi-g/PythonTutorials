from pprint import pprint

class Mammal:
    def __init__(self):
        pprint("This is Mammal")
    def move(self):
        pprint("I am moving")

    def run(self):
        pprint("I am running")

class Bird:
    def __init__(self):
        pprint("This is bird")

    def fly(self):
        pprint("I am flying")

class Bat(Mammal, Bird):
    pass

aBat = Bat()
aBat.move()
aBat.run()
aBat.fly()