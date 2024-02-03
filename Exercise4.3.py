numbers = []

while True:
    number_input = input("Enter a number (or press Enter to quit): ")

    if number_input == "":
        break

    number = float(number_input)
    numbers.append(number)

if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print("Smallest number:", smallest)
    print("Largest number:", largest)
else:
    print("No numbers were entered.")