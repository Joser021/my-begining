# normal assignment
# it calculates the area of a square
print()
square_length = float(input("What is the length of a side of the square? "))
square_area = square_length ** 2
print(f"The area of the square is: {square_area}")
print()

# it calculates the area of a rectangle
rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of rectangle? "))
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {rectangle_area}")
print()

# it calculates the area of a circle
circle_radius = float(input("What is the radius of the circle? "))
circle_area = 3.14 * circle_radius ** 2
print(f"The area of the circle is: {circle_area}")
print()



# first streched assignment: Library
import math
print()
circle_radius = float(input("What is the radius of the circle? "))
circle_area = math.pi * circle_radius ** 2
print(f"The area of the circle is: {circle_area:.2f}")
print()



#second strech assignment: The Same Value
import math

#prompt from the user
print()
side = float(input("What is the length of a side of the Square? "))

#result of the calculations
square_area = side ** 2
print(f"The area of the square is: {square_area:.2f}")

circle_area = math.pi * side ** 2
print(f"The area of the circle is: {circle_area:.2f}")

cubic = side ** 3
print(f"The cubic value is: {cubic:.2f}")

sphere = 4 / 3 * math.pi * side ** 3
print(f"The sphere value is: {sphere:.2f}")
print()




#Third stretch assignment: Centimeter -> Meters
print()
square_length = float(input("Insert the length of a square in centimeters: "))
square_cm2 = square_length ** 2
square_m2 = square_cm2 / 10000
print(f"""The are of the square is:
{square_cm2} cm²
{square_m2} m²
""")

# it calculates the area of a rectangle
rectangle_length = float(input("Insert the length of a rectangle in centimeters: "))
rectangle_width = float(input("Insert the the width of a rectangle in Centimeters: "))
rectangle_cm2 = rectangle_length * rectangle_width
rectangle_m2 = rectangle_cm2 / 10000
print(f"""The area of the rectangle is:
{rectangle_cm2}cm²
{rectangle_m2}m²
""")

# it calculates the area of a circle
circles_radius = float(input("Insert the radius of the circle in Centimeters: "))
circles_cm2 = 3.14 * circles_radius ** 2
circles_m2 = circles_cm2 / 10000
print(f"""The are of the circle is:
{circles_cm2}cm²
{circles_m2}m²
""")

