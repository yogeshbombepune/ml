# Conditionals
num1 = 10
num2 = 14
num3 = 17

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
elif num2 > num3:
    if num2 > num1:
        print(num2)
    else:
        print(num1)
else:
    print(num3)

# switch case

# for loop

for val in range(0, 8):
    print(val)

for val in [1, 2, 3]:
    print(val)

for val in sorted([1, 3, 4, 5]):
    print(val)

# reverse
for val in reversed([5, 3, 9, -1]):
    print(val)

# While
n = 10
while n:
    print(n, end=' ')
    n = n - 1
print('Done')

# Data Structure
# Sequences
# Lists
# mutable, possible heterogeneous, ordered,nestable

l = ['U', 'Z', 'H']
l[2] = 'G'
print(l)

l[1: 3] = ['a', 'b']
print(l)

l[-1: -2] = ['x', 'y']
print(l)

l[2:] = range(5)
print(l)

# remove based on value and first occurrence
l.remove(0)

# pop
l.pop(1)
print(l)

# * is used to repeat the things
l = [1, 2]
print(l*3)

# in operator

l = [12,23,32]
flag =12 in l
print(flag)

# zip for lists together
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for i, j in zip(list1, list2):
    print(i, j)
# Argument Unpacking

pairs = [('a', 1)]
print(zip(*pairs))

# list comprehensions
data = []
for num in range(6):
    print(num*num)

data = [num*num for num in range(6)]
print(data)

data = [num*num for num in range(6) if num % 2 == 0]
print(data)

# open("").readline()




# tuple  immutable use () to define
t = (1, 2, 3)
print(t[0])
print(t[0:1])
# t[0] = 5 not permitted
print(t)


a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)

# print(type(a, b, c))

# Containers
# Sets and dictionaries

some_set = {4, 4, 1, 2, 3, 4}
print(len(some_set))
print(some_set)

# creating empty set
empty_set = set()
empty_set.add(1)
empty_set.add(2)
empty_set.add("Yes")
print(empty_set)

set_A = {1,2,3,4,5}
set_B = {4,5,6,7}
print("Set A",set_A)
print("Set B",set_B)
print("Diff A - B",set_A )
print("Intersection",set_A.intersection(set_B))
print("Union",set_A.union(set_B))
print("Symantric",set_A ^ set_B)


# Dictionaries use  {} to define
# key value pair
D = {}
D['a'] = 1
D[2] = 'b'
print(D)

D = {'a' : 1, 2 : 'b'}
print(D)


# Default Dict


# Counter

#