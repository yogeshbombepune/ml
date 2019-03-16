# Functions
import random
import math

print(list(range(-10, 10, 2)))

a = [0.819, 0.277, 0.817, 0.575, 0.168, 0.973, 0.987, 0.883, 0.293, 0.933]
b = [round(num, 2) for num in a if num > 0.5]
print(sorted(b))


# signature

# def function_name(Parameter list);

def in_range(number, a, b):
    if number >= a and number <= b:
        return True
    return False


def factorial(number):
    fact = 1
    i = 1
    for i in range(i, number + 1):
        fact *= i
    return fact


def fibonacci(number):
    num1 = 0
    num2 = 1
    list_of_fibonacci = []
    for num in range(0, number + 1):
        list_of_fibonacci.append(num1)
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    print(list_of_fibonacci)


def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# shuffle

def shuffle_list(listA):
    random.shuffle(listA)
    return listA


list_of_numbers = [5, 10, 2, 1, 3]


# def binary_search(list_of_numbers, num):
#    bottom = 0
#    top = len(list_of_numbers) -1
#    index = -1
#    while top>=bottom and index==-1:
#         print(top)
#
#
#
#
#
# #print(binary_search(list_of_numbers, 5))


def compute(num, to=4):
    sum = 0
    for n in range(1, to):
        sum = sum + num
        num = num * 11
    return sum


# defaulting arg
# def hello(name='word')


print("Compute: ", compute(3))
print(shuffle_list([3, 6, 7, 8]))

print(fibonacci(8))
print(factorial(5))
print(fib(8))
print(in_range(10, 5, 11))
print(in_range(2, -10, 5))


# Call by value and reference

# Exception

# try:
#     # code
# except Exception:
#     # kjl
# finally:
#     # kjll

def div(aa, bb):
    try:
        if bb == 0:
            raise ZeroDivisionError
        return aa / bb
    except ZeroDivisionError as e:
        print(e)
        return aa / (bb + 1)
    finally:
        print("clean every thing..")


print(div(5, 0))

# File IO

f = open("temp.txt", "w")
for num in range(25):
    f.write(str(num) + '\n')
f.close()

with open("temp.txt", "r") as f:
    numbers = [int(num) for num in f if len(num) > 0]
print(numbers)

f = open("euro.csv")
d = {}
# print(f.readlines())
for line in f.readlines():
    (key, val) = line.split(",")
    d[key] = val.strip()
print(d)


def unique_words(d):
    print(d)
    for pairs in d:
        d.values();
        d.keys();



f = open("lorem_ipsum.txt", "r")
d = {}
for line in f.readlines():
    pair = line.split(" ")
    for word in range(len(pair)):
        if pair[word].strip() in d:
            d[pair[word].strip()] = d[pair[word].strip()] + 1
        else:
            d[pair[word].strip()] = 1

unique_words(d)

print(d)
