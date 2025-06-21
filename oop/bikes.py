class Bikes:
    def __init__(self, brand, bkname, rent):
        self.brandname = brand
        self.__bikename = bkname #private
        self.rentperday = rent

    @property       # to access we use getter and setter method in python
    def bikename(self):
        return self.__bikename

    @bikename.setter
    def bikename(self,value):
        self.__bikename = value

    def calculate_rent(self, days):
        return self.rentperday * days

