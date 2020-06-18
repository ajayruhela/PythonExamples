x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()

def outer():
    x = "local"

    def inner():
        global x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)
