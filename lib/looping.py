#!/usr/bin/env python3

def happy_new_year():
    countdown = list(range(10, 0, -1))
    for number in countdown:
        print(number)
    print("Happy New Year!")
    pass

def square_integers(int_list):
     return [num ** 2 for num in int_list]

if __name__ == "__main__":
    int_list = [1, 2, 3, 4, 5]
    squared_nums = square_integers(int_list)
    print(squared_nums)
    pass

def fizzbuzz():
     for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    

if __name__ == "__main__":
    happy_new_year()
    squared_nums = square_integers([1, 2, 3, 4, 5])
    print(squared_nums)
    fizzbuzz()