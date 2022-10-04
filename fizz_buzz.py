#!/usr/bin/env python3.7

#Lab exercise

upper_number = int(input("How may values should we process?: "))

for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)