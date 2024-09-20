
# Zunair Shahid First Project of Codex Cue Python Development internship program

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    sub = numbers[0]
    for num in numbers[1:]:
        sub -= num
    return sub

def multiply(numbers):
    mul = 1
    for num in numbers:
        mul *= num
    return mul

def divide(numbers):
    div = numbers[0]
    try:
        for num in numbers[1:]:
            div /= num
    except ZeroDivisionError:
        return "Error, Zero division is not possible "
    return div

def simple():
    print()
    print("Zunair Shahid First Project of Codex Cue Python Development internship program ")
    print("--------------Simple Calculator by using Python--------------")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")   
        select = input("Select: \n")
        if select == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if select in ['1', '2', '3', '4']:
            try:
                numbers = list(map(float, input("Enter numbers by using space: ").strip().split()))
                if len(numbers) < 2:
                    print("Please enter at least two numbers.")
                    continue
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if select == '1':
                print(f"The result of Addition is: {add(numbers)}")

            elif select == '2':
                print(f"The result of Subtraction is: {subtract(numbers)}")

            elif select == '3':
                print(f"The result of Multiplicationis: {multiply(numbers)}")

            elif select == '4':
                result = divide(numbers)
                print(f"The result of Division is: {result}")     
        else:
            print("Invalid Input! Please select a valid option.")
simple()
























         









