from oop.bikes import Bikes

brand = input('Brand ')
bknm =  input('Bike name ')
rpd = int(input('Rent '))

bkobj = Bikes(brand = brand, rent = rpd , bkname= bknm)

days = int(input('No of days '))
print(f'Bike {bkobj.bikename} for {days}  is {bkobj.calculate_rent(days)}')