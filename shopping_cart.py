
# lists used by the program
items = []
prices = []
items_amount = []

print("Welcome to the Shopping Cart Program!")

# while loop to make the code loop, unless the user types 5
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

# if statemants for the options
    if action == 1:
        add_item = str(input("What item would you like to add? "))
        price = float(input(f"What is the price of '{add_item}'? "))
        number_of_items = int(input("What is the amount of items? "))

        amount = price * number_of_items # calculates the amount of items

    # it adds to its respective lists
        items.append(add_item)
        prices.append(amount)
        items_amount.append(number_of_items)
        print(f"'{add_item.capitalize()}' has been added to the cart.")
    
    elif action == 2:
        print("The contents of the shopping cart are:")

    # it displays the items in the list
        for i in range(len(items)):
            print(f"{i + 1}. {items[i].capitalize()}({items_amount[i]}) - ${prices[i]:.2f}")
    
    elif action == 3:
        print("The contents of the shopping cart are:")

    # it displays the items in the list
        for i in range(len(items)):
            print(f"{i + 1}. {items[i].capitalize()}({items_amount[i]}) - ${prices[i]:.2f}")
        
        remove_item = int(input("Which item would you like to remove? "))
        print("Item removed.")

        # it removes the items in the lists
        remove = remove_item - 1
        items.pop(remove)
        prices.pop(remove)

# it calculates the total price
    elif action == 4:
        total = 0
        for i in prices:
            total += i
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    elif action == 5:
        break
    
print("Thank you. Goodbye.")
