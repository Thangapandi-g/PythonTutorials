class Customer:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.__age = 18 #private variable

    def get_age(self):
        return self.__age