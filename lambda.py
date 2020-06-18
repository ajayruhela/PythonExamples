# Program to show the use of lambda functions
def func_1():
    return "Hello"

double = lambda x: x * 2

print(double(5))

temp = lambda y: y()
print(temp(func_1))

temp1 = lambda z,y:z+y
print(temp1(2,y=3))

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

in_tp= (1,2,3,4,5)
sq_tpres = tuple(map(lambda x: x**2 , in_tp))

print(sq_tpres)
