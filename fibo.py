n= int(input('enter number of Fib numbers you want, should be <1000'))
a=0
b=1
if n< 1000:
    while(n>0):
        print(b)
        b=a+b
        a=b-a
        n-=1
print('ends')

        
    
