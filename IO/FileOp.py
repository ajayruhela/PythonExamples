with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
   
try:
   f = open("test.txt",'a', encoding = 'utf-8')
   f.write("contains three lines2\n")
finally:
   f.close()

try:
    f = open("test.txt",'r',encoding = 'utf-8')
    print(f.read(4))
    print(f.tell())
    print(f.seek(0))
finally:
    f.close()
    
f = open("test.txt",'r',encoding = 'utf-8')
for line in f:
        print(line, end = '')
f.close()
    
f = open("test.txt",'r',encoding = 'utf-8')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
    
f = open("test.txt",'r',encoding = 'utf-8')
print(f.readlines())
