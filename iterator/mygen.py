# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
#use >>> a= my_gen()
# then call next(a)
#else
# Using for loop
for item in my_gen():
    print(item)
