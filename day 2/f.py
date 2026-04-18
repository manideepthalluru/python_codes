"""
def sum(a,b):
    print(a+b)
sum(2,3)

    
def abc():
    print("hello world")

abc() # it returns hello world as output

"""

#oops - object oriented programming language

#class, object

"""
class First:
    a = 78

    def method1(self):      #self must be included when defining the function in the class
        print("Method1")

o1 = First()    #object

print(o1.a)
o1.a = 80
print(o1.a)
o1.method1()

#inheritance concept    (parent and child)

class second(First):
    b = 45
    
    def method2(self):
        print("Method2")

s1 = second()
print(s1.b)
print(s1.a)

"""

#module

"""
import module1

module1.add(2,4)

"""

import module1 as m     # if module name is big, we can use it to have short name for module
m.add(2,3)

from module1 import add     #this will import only add function from the module1
add(4,3)

from module1 import *       #this will import all functions from the module1

add(3,2)
sub(3,2)
multi(3,2)
div(3,2)


