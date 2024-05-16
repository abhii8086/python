# two type of conversion
'''
1.implicit:by interpreter
2.explicit:by user
'''
# explicit
# int() , float() ,str()
'''int<-->float'''
a = 5.5
print(int(a))

b = 9
print(float(b))

'''int<--str'''
d = '5'
print(type(d),d)
d = int(d)
print(type(d),d)
