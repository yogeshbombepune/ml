def times_two(inp):
    inp = 2 * inp
    return inp


varible_A = 10
print(times_two(varible_A))
print(varible_A)


# when use globle it will reflacted outside.

def f():
    global s
    s = "I am globally not known"
    print(s)


f()
print(s)


