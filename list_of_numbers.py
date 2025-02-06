series_of_numbers = []
positive_numbers = []
sum = 0
largest = 0
smallest = 0

print()
print("Enter a list of numbers, type 0 when finished.")
while True:
    number = int(input("insert a number: "))
    
    if number != 0:
        series_of_numbers.append(number)
    
    else:
        break

for i in series_of_numbers:
    sum += i

    if i > 0:
        positive_numbers.append(i)
        smallest = min(positive_numbers)

        largest = max(positive_numbers)

average = sum / len(series_of_numbers)

sorted_list = sorted(series_of_numbers)

print()
print(f"The sum is: {sum}")
print(f"The aerage is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest positive number is: {smallest}")

print("The sorted list is:")
for i in sorted_list:
    print(i)
