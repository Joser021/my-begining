print()
print("-=-" * 15)
child_meal = float(input("What is the price of a Child's Meal? "))
adult_meal = float(input("What is the price of an adult's Meal? "))

children_amount = int(input("how many children are there? "))
adult_amount = int(input("how many adults are there? "))




# strech challenge

#asking for drink
drink = float(input("What is Drink's price? "))
if drink == 0:
    print("No Drink $0.00")
else:
    print(f"Drink: ${drink:.2f}")

# dessert
dessert = float(input("What is the Dessert's price? "))
if dessert == 0:
    print("No Dessert $0.00")
else:
    print(f"Dessert: {dessert:.2f}")

#subtotal, sales taxes and total
print()
subtotal = (child_meal * children_amount) + (adult_meal * adult_amount) + drink + dessert
print(f"\033[31mSubtotal:\033[m ${subtotal:.2f}")

print()
tax = int(input("What is the sales tax rate? "))
sales_tax = (tax / 100) * subtotal
print(f"Sales Tax: ${sales_tax:.2f}")

print()
total = subtotal + sales_tax
print(f"\033[31mTotal:\033[m ${total:.2f}")


# print()
# change = float(input("What is the payment amount? "))
# print(f"\033[33mChange:\033[m ${change - total:.2f}")
# print("-=-" * 15)
# print()


# personalize this calculator meal, i trust in you man
