# normal assignment
# it calculates the are of a square
sqr_length = float(input("What us the length of a side of the square? "))
sqr_area = sqr_length ** 2
print(f"The are of the square is: {sqr_area}\n")

# it calculates the area of a rectangle
rec_length = float(input("What is the length of rectangle? "))
rec_width = float(input("What is the width of rectangle? "))
rec_area = rec_length * rec_width
print(f"The area of the rectangle is: {rec_area}\n")

# it calculates the area of a circle
cir_radius = float(input("What is the radius of the circle? "))
cir_area = 3.14 * cir_radius ** 2
print(f"The are of the circle is: {cir_area}\n")



#first steched assignment
import math

#prompt from the user
print(f"{math}")
length = float(input("what is the length you want to insert in? "))
pi = math.pi

#result of the calculations
square_area = length ** 2
print(f"The area of the square is: {square_area:.2f}")

circle_area = pi * length ** 2
print(f"The area of the circle is: {circle_area:.2f}")

cubic = length ** 3
print(f"The cubic value is: {cubic:.2f}")

sphere = 4 / 3 * pi * length ** 3
print(f"The sphere value is: {sphere:.2f}")




# it calculates the are of a square
sqr_length = float(input("Insert the length of a square in centimeters: "))
sqr_cm2 = sqr_length ** 2
sqr_m2 = sqr_cm2 / 10000
print(f"""The are of the square is:
{sqr_cm2} cm²
{sqr_m2} m²\n""")

# it calculates the area of a rectangle
rec_length = float(input("Insert the length of a rectangle in centimeters: "))
rec_width = float(input("Insert the the width of a rectangle in Centimeters: "))
rec_cm2 = rec_length * rec_width
rec_m2 = rec_cm2 / 10000
print(f"""The area of the rectangle is:
{rec_cm2}cm²
{rec_m2}m²\n""")

# it calculates the area of a circle
cir_radius = float(input("Insert the radius of the circle in Centimeters: "))
cir_cm2 = 3.14 * cir_radius ** 2
cir_m2 = cir_cm2 / 10000
print(f"""The are of the circle is:
{cir_cm2}cm²
{cir_m2}m²""")
