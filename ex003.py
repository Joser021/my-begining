#badget ID
print("Please enter the following information:")
# it ask for the person's data
first = str(input("First name: "))
last = str(input("Last name: "))
email = input("Email address: ")
phone = input("Phone Number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")
hair = input("Hair: ")
yeys = input("Yeys: ")
month = input("Month: ")
training = input("Training (Yer or No): ")

#it displays the person's data
print("\nThe ID Card Is:")
print("--" * 20)
print(f"{last.upper()}, {first.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}\n")

print(email.lower())
print(phone)

print(f"\nHair: {hair.capitalize():15} Yeys: {yeys.capitalize()}")
print(f"Month: {month.capitalize():14} Training: {training.capitalize()}")
print("--" * 20)