print("Hello World.")

#   comments by Hash

# line
# jouj
# njn

minute = 10
percentage = (minute * 100)
if percentage == 1001:
    print("same")
print(percentage)

# pointing references
x = 5;
y = x;
print("x:", x);
print("y", y);
x = 10;
print("x:", x)
print("y", y);

x = "Text"
print("x:", x)

# All variables are references
a = [1, 2, 3]
b = a
b.remove(2)
print("a", a)
print("b", b)
print(id(a))
print(id(b))

#
a = 1;
b = a
b += 1
print(a)
print(b)

# id is used to get memory location
print(id(a))
print(id(b))

#  Dyanamic Types
pi = 3.14
print(type(pi))
pi = "Strign"
print(type(pi))
pi = '2'
print(type(pi))

# variable names error


# data types
# bool
# int
# long
# float
# str
# list
# tuple ()
# set {}
# dict  {}


# Integer
print(1, 00, 000)
print(1, 00, 000 + 1, 0, 0 + 2, 5, 9)

# Boolean
flag = True
flag = False

# String
a = "hkhkhlhk"
a = "jkhkjh'bghjghj"

# tipple quotes for multi line

word = "Python"
print(type(word))
print(word[0])
print(word[1])
print(word[5])
print(word[-1])  # last character
print(word[0:2])
print(word[2:4])
print(word[3:])
print(word[-3:-1])

# excercise
sentence = "dealing with Data"
print(sentence[0:3])
print(sentence[-6:-1])

# String functions
# startswith
print(sentence.startswith("e"))
print(sentence.endswith("r"))

# Only first character
print(sentence.capitalize())

# first World capital
print(sentence.title())
print(sentence.lower())
print(sentence.upper())

# split
splitedWord = sentence.split(' ')
print(splitedWord)
joinedSentence = ",".join(splitedWord)
print("Joind ", joinedSentence)

# replace
print(sentence.replace("D", "M"))
print(sentence)

# lstrip() rstrip() strip() its like trim() in java


# finding text

word = "And on and on and on and on...."
ind = word.find("on");
print(ind)  # return start index
secondOccurrence = word.find("on", ind + 1)
print(secondOccurrence)

midPoint = int(len(word) / 2)
print(midPoint)

# count
wordCount = word.count("And")
print(wordCount)

# String comparison ==
email = "billgates@microsoft.com"
separation = email.split("@")
print("Name: ", separation[0])
print("Company Name: ", separation[1].split(".")[0])
print("Domain: ", separation[1].split(".")[1])

# String formatting
print("Coordinates: {}, {}".format("31.09N", "34.89W"))
print("Latitude: {0}, Langitude: {1} ==> [{0}, {1}]".format("31.23N", "23.43W"))
# print("Latitude: {}, Langitude: {} ==> [{}, {}]".format("31.23N","23.43W"))

# Naming the order
print("Coordinates: ")

# concat using +

# multiplication on string  its repeat behaviour
print("xxx" * 3)

# String length finding
print(len("xxx"))

# swap
a = "Apple"
b = "ball"
print(a)
print(b)
temp = a
a = b
b = temp
print(a)
print(b)

#  in python
a = "Apple"
b = "ball"
a, b = b, a
print(a)
print(b)

print(a.isalpha())
print(a.isalnum())
print(a.isdecimal())
print(a.isnumeric())
print(a.isdigit())

# Operators
# and or not
# <><===!=
print(2**38);
print(pow(2,38))

# division on String not alllowed


# division using / and //
# / division
# // floor division
print(11/2)
print(11//2)

# mod % to get remainder

# is operator is equality
a =1
b = 1
print(a is b)


sentence = "mea"
if(len(sentence)>3):
    if(sentence.endswith("ing")):
        print(sentence+"ly")
    else:
        print(sentence+"ing")
else:
    print(sentence)


