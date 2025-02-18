from math import pi
from time import sleep

def compute_area_square(side):
    area_square = side * side
    return area_square
    # or you can just do => Return side * side

def compute_area_rectangle(length, width):
    area_rectangle = length * width
    return area_rectangle
    # or you can just do => Return length * width

def compute_area_circle(radius):
    area_circle = pi * (radius ** 2)
    return area_circle
    # or you can just do => Return  pi * (radius ** 2)

while True:
    sleep(1)
    print(f"""
Find the Area of a Shape:
{"-=-" * 5}
- Square
- Rectangle
- Triangle

You can type QUIT to leave the program
{"-=-" * 5}
        
    """)

    choose_shape = str(input("Which area do you want to find? ")).lower()

    if choose_shape == "square":
        result = compute_area_square(float(input("What is the SIDE of the Square? ")))
        print(f"The area of the Square is: {result}")
    
    elif choose_shape == "rectangle":
        result = compute_area_rectangle(float(input("What is the LENGTH of the Rectangle? ")), float(input("What is the WIDTH of the rectangle? ")))
        print(f"THe area of the Rectangle is: {result}")

    elif choose_shape == "circle":
        result = compute_area_circle(float(input("What is the RADIUS of the Circle? ")))
        print(f"The area of the circle is: {result:.4f}")

    elif choose_shape == "quit":
        print("Thank you for using. see ya")
        break
    
    else:
        print("Sorry, I didn't understand. Please, Try Again.")