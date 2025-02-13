# core requirements
with open("hr_system.txt") as people_data:
    for line in people_data:
        stripped = line.strip()
        splitted = stripped.split(" ")

        print(f"Name: {splitted[0]}, {splitted[2]}")


# stretch challenge
with open("hr_system.txt") as people_data:
    for line in people_data:
        stripped = line.strip()
        splitted = stripped.split()
        salary = float(splitted[3])

        pay_check = salary / 24

        if splitted[2] == "Engineer":
            pay_check += 1000

        print(f"Name: {splitted[0]} (ID: {splitted[1]}), {splitted[2]} - ${pay_check:.2f}")

