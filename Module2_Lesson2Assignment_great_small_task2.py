# Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

numbers = input("Enter three numbers separated by spaces: ")

# Even though numbers should be registered as int, because input variable is in code, numbers will register as string. To counter this numbers have to get splitted (due to spacing so three numbers can register in the same line). Then to convert numbers back to integers, map(int) function will be used to bring it all back. Comparision strings are added to find greatest and smallest number with number user inputs.

number1, number2, number3 = map(int, numbers.split())
greatest_number = number1
smallest_number = number1

if number2 > greatest_number:
    greatest_number = number2
if number3 > greatest_number:
    greatest_number = number3
print(greatest_number, "is the largest number.")

# Task 2 Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.
if number2 < smallest_number:
    smallest_number = number2
if number3 < smallest_number:
    smallest_number = number3
print(smallest_number, "is the smallest number.")
