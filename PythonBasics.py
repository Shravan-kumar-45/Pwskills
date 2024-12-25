from operator import truediv

print("Hello World")
# Predefined Objects , keywords & Identifier


print("Hello World") # Open and Close brackets

a = 3 # Here A is a variable
# variable are placeholder where we will keep variety of data which we can use to write code.

print(type(a)) # here 'a' is a integer

b= 4.4 # it is a float
print(type(b))

c= " shravan"
print(type(c))
d= True
print(type(d))

e = True - False
print("Type of e",type(e))

f = 34 -67j
print(type(f))

print(f.real) # to  find real part of the complex number
print(f.imag) # to find imaginary part of complex number

'''Rules of defining variable start with letter or underscore and instead of space use underscore
12iinn in vaild
_renfe12 vaild'''

# Always try to name variable which make sense
# Never use keywords as variable
#keywords in python are predefined words

help('keywords') # tools help to get predifined keywords which we never used as variable beacause it will rededifined the variable with new one.

# indentation help to tool to identify which block of code belong to which part of the condition


#Idexing
a= "Shravan"
print("Index of shravan at position 3 and -5: " ,a[3],a[-5])

#another type of data container
list_container = [1,2,3,"kumar",True,"z"]
print(list_container,type(list_container))

print( list_container[3])
list_container[3]= "shravan"
print(list_container)

#Objects/ container whose state or value can be changed after they are created are called mutable.
# container whose state or value can not be changed after they are created are called immutable.
