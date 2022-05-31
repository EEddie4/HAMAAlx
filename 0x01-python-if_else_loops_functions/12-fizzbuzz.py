#!/usr/bin/python3

mot = ""


def fizzbuzz():
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            mot = "FizzBuzz"
        elif num % 3 == 0:
            mot = "Fizz"
        elif num % 5 == 0:
            mot = "Buzz"
        else:
            mot = str(num)
        print(mot, end=" ")
    print("Buzz")
