from ast import While
import numbers
from tokenize import Number


def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

while True :
	print("Please select operation -\n" \
			"1. Add\n" \
			"2. Subtract\n" \
			"3. Multiply\n" \
			"4. Divide\n" \
			"5. Close\n")
			
	select = int(input("Select operations form 1, 2, 3, 4, 5:"))
	if select == 1:
		number_1 = int(input("Enter first number: "))
		number_2 = int(input("Enter second number: "))
		print(number_1, "+", number_2, "=",
						add(number_1, number_2))

	elif select == 2:
		number_1 = int(input("Enter first number: "))
		number_2 = int(input("Enter second number: "))
		print(number_1, "-", number_2, "=",
						subtract(number_1, number_2))

	elif select == 3:
		number_1 = int(input("Enter first number: "))
		number_2 = int(input("Enter second number: "))
		print(number_1, "*", number_2, "=",
						multiply(number_1, number_2))

	elif select == 4:
		number_1 = int(input("Enter first number: "))
		number_2 = int(input("Enter second number: "))
		print(number_1, "/", number_2, "=",
						divide(number_1, number_2))
	elif select == 5:
		break					
	else:
		print("Invalid input")
		
		
 


    