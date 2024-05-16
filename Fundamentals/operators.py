# (6) types of oprator in python 

# 1.Arithmetic Operators
a,b = 10,5
print(a + b) 
print(a - b )
print(a * b )
print(a / b )
# floor division
print(a // b) 
print(a % b )
# power a^b
print(a**b)

# 2.Assignment Operators
x = 10
y = 9
x += y     
print(x)

# 3.Comparison Operators
a = 5

b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)


# 4.Logical Operators
# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False


# 5.Bitwise Operators
'''
Operator	Meaning	            Example
&	        Bitwise AND	        x & y = 0 (0000 0000)
|	        Bitwise OR	        x | y = 14 (0000 1110)
~	        Bitwise NOT	        ~x = -11 (1111 0101)
^	        Bitwise XOR	        x ^ y = 14 (0000 1110)
>>	        Bitwise right shift	x >> 2 = 2 (0000 0010)
<<	        Bitwise left shift	x 0010 1000)
'''
# 6.Special Operators
# idenitiy oprator
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False

# membership operator
message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False