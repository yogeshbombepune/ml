# comprehensions
data = [str(val) for val in range(2000, 3200) if val % 7 == 0 and val % 5 != 0]
print(data)

# count character
import collections

name = "google.com"
char_count_dict = {}
for ch in name:
    if ch not in char_count_dict.keys():
        char_count_dict[ch] = 1
    else:
        char_count_dict[ch] = char_count_dict[ch] + 1

print(char_count_dict)

from collections import Counter

c = Counter(name)
print(c)

od = collections.OrderedDict(sorted(char_count_dict.items()))
print(od)

# print common keys and common values
a_dict = {"a": "e", "b": 5, "c": 3, "d": 4}
b_dict = {"c": 5, "d": 6}

print("Common keys:", set(a_dict.keys()).intersection(set(b_dict.keys())))
print("Common Values: ", set(a_dict.values()).intersection(set(b_dict.values())))
print("Common keys", [m for m in a_dict if m in b_dict])
print("Common Values", )

#
x = {}
for i in range(1, 8):
    x[i] = i * i
print(x)

# swap key and values together
D = {"CH": "Switzerland", "I": "Italy", "F": "France"}
Dinv = dict((v, k) for k, v in D.items())
print(Dinv)
print(Dinv.get("Italy", 5))  # default value if key is not present.

document = "Yogesh Bombe"
print(Counter(document.split()))
