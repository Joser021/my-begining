items = []

print("Welcome to the Shopping Cart Program!")

while True:
    print("""
Please select one of the following:
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
    """)
    action = int(input("Please enter an action: "))

    if action == 1:
        add = str(input("What item would you like to add? "))
        items.append(add)
        print(f"'{add}' has been added to the cart.")
    
    elif action == 2:
        print("The contents of the shopping cart are:")
        for i in items:
            print(i)
    
    
    elif action == 5:
        break
    
print("Thank you. Goodbye.")