# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:28:03 2017

@author: Nitin
"""


###################### ADDITION OF COMPLEX NUMBER IN PYTHON #################### 

class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10

# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'





################# FUNCTION OVERRIDDEN IN PYTHON using inheritance #######################



class Parent:        # define parent class
   def myMethod(self):
      print 'Calling parent method'

class Child(Parent): # define child class
   def myMethod(self):
      print 'Calling child method'

c = Child()
p = Parent()
c.myMethod()          # instance(object) of child
p.myMethod()         # child calls overridden method


############################## INVOCATION OF PRIVATE METHODS IN PYTHON #########

class Point(object):
    def __init__(self,x=0,y=0):
        self.x,self.y=x,y
        self.__z=0
        print "Object created with",
        self.printDetails() # private method invoked from within class
    def printDetails(self):
        print self.x,self.y,self.__z

pt=Point()
pt.printDetails()  # private method invoked from outside class (will give error)




############    LIST COMPREHENSION    #####################


pow2=[x**2 for x in range(10)]
print pow2


pow3=[2**x for x in range(11)]
print pow3



mul=[ x*y for x in range(1,4) for y in range(2,5)]
print mul





list = [1,2,3,4,5,6,7,8]
multiply=[x*4 for x in list]
print multiply



list = [1,2,3,4,5,6,7,8]
print len(list)



string=[1,2,3,4,5,6,7,8,9]
print (string)



for letter in set("apple"):
    print letter
