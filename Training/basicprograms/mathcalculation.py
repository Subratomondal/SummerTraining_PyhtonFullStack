from calc.mymathcalc import area_of_circle, circuference_of_circle, area_of_sq

radius = int(input("Enter the radius of circle: "))
print(f'Area of Circle: {area_of_circle(radius)}')
print(f'Circumference of Circle: {circuference_of_circle(radius)}')

side = int(input('Side: '))
print(f'Area of Square: {area_of_sq(side)}')