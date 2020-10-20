# Eric Browne
# January 21st Notes: Tuesday Week 3

#a=5
#print(id(a))
#a= 10

#print(id(a))
#a="hello"
#print(id(a))

#alias
#b=a
#print(id(b))   #b now has the same value as a
#b=5
#a=5
#print(id(b), id(a))  #Still the same value!


#a = 2**1000
#b = 2**1000
#print(id(a))
#print(id(b))
#print(a is b)
#print(a == b)


#def swap(a,b):
#    a,b=b,a
#a =5
#b = 10
#swap(a,b)
#print(a)
#print(b)


# A class is just a template for an object
class MyClass:
    def __init__(self,my_list,my_string):
        self.my_list = my_list
        self.my_string = my_string
li=[1,2,3]
a = MyClass(li,"hello")
b=a
