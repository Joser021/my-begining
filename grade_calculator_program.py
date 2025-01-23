from time import sleep

print()
print("-=-" * 13)
grade_percentage = int(input("\033[31mWhat is the percentage of your grade?\033[m\n"))
print()

print("Processing...")
sleep(1)

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
    letter = "f"
print(f"\033[33mYour Grade is:\033[m {letter}")
print("-=-" * 5)
print()

if grade_percentage >= 60:
    print(f"""\033[31mYour grade is really good! You passed!\033[m
\033[33mCongratulations!\033[m
{"-=-" * 13}
          """)
