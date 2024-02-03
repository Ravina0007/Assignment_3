while True:
    inches = float(input("Enter the number of inches (or a negative value to quit): "))

    if inches < 0:
        break

    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters.")

print("Program ended.")