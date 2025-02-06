# list and stored the program will use
list_of_numbers = []
positive_numbers = []
sum = 0
largest = 0
smallest = 0

# code's beginning
print()
print("Enter a list of numbers, type 0 when finished.")

# while loop asking for the numbers of a list
while True:
    number = int(input("Enter the number: "))

    # if will store the numbers in the list_of_numbers
    if number != 0:
        list_of_numbers.append(number)
        
    # it will stop the loop
    else:
        print()
        break

# the loop for will print the number one-by-one
for i in list_of_numbers:
    sum += i # it will sum the numbers of the list

    # the largest numbers and the smallest positive number 
    if i > 0:
        positive_numbers.append(i)
        largest = max(list_of_numbers) # largest number
        smallest = min(positive_numbers) # smallest number

average = sum / len(list_of_numbers) # it will calculate the average

sorted_list = sorted(list_of_numbers) # it will make our sorted list

# it will the results, sum, average, largest number, smallest number
print(f"The sum is: {sum}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest positive number is: {smallest}")

# it will print the sorted list
print("The sorted list is: ")
for i in sorted_list:
    print(i)
