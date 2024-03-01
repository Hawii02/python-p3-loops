#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    # squares = [abs(num) ** 2 for num in int_list]
    squares = list()
    for num in int_list:
        square = num **2
        squares.append(square)
    return(squares)


def fizzbuzz():
    i = 1
    while i < 101:
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
            i += 1
        elif i % 3 == 0:
            print("Fizz")
            i += 1
        elif i % 5 == 0:
            print("Buzz")
            i += 1
        else:
            print(i)
            i += 1
print()   
