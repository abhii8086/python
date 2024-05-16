# if else greater of 3 no 
a,b,c = 3,2,5
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)
   
# if elif  grade  of student
marks = 90

if(marks>90):
    print("A")
elif(marks>75):
    print("B")
else:
    print("C")

# ternary oprator
x = 1
y = 2
result = x if (x > y) else y
print(result)
