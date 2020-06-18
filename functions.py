def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)
    print(type(names))

def greet1(in_list):
    for name in in_list:
        print("Hi!",name)
    print(type(in_list))

greet("Ajay","Kumar","Ruhela")
greet1(['Ajay','A1','A2'])
greet1({1:'Ajay',2:'A1',3:'A2'})

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print("The factorial of", num, "is", factorial(num))
