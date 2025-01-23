# Core requirements
from time import sleep

#promting the grade
print()
print("-=-" * 13)
grade_percentage = int(input("\033[31mWhat is the percentage of your grade?\033[m\n"))
print()

#it delays letter grade for 1 second
print("Processing...")
sleep(1)

#it will check it letter is the grade depending on the condition
print("-=-" * 5)
if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"
print(f"\033[33mYour Grade is:\033[m {letter}")
print("-=-" * 5)
print()

if grade_percentage >= 70:
    print(f"""\033[31mYour grade is really good! You passed!\033[m
\033[33mCongratulations!\033[m
          """)
else:
    print("""\033[31mI'm sorry, you didn't passed,\033[m
Good Luck next time!
          """)
print("-=-" * 13)

# strech challenge
from time import sleep

#promting the grade
print()
print("-=-" * 13)
grade_percentage = int(input("\033[31mWhat is the percentage of your grade?\033[m\n"))
print()

# "+" or "-"
remainder = grade_percentage % 10

if grade_percentage >= 93 or grade_percentage < 60:
    sign = ""
else:
    if remainder >= 7:
        sign = "+"

    elif remainder < 3:
        sign = "-"

    else:
        sign = ""


#it delays letter grade for 1 second
print("Processing...")
sleep(1)

#it will check it letter is the grade depending on the condition
print("-=-" * 5)
if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"
print(f"\033[33mYour Grade is:\033[m {letter}{sign}")
print("-=-" * 5)
print()

if grade_percentage >= 60:
    print(f"""\033[31mYour grade is really good! You passed!\033[m
\033[33mCongratulations!\033[m
          """)
else:
    print("""\033[31mI'm sorry, you didn't passed,\033[m
Good Luck next time!
          """)
print("-=-" * 13)
