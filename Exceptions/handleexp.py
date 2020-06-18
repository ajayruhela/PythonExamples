import sys

randomList = ['a', 0, 2, 4]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        print("The reciprocal of", entry, "is", r)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
#print("The reciprocal of", entry, "is", r)

# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
