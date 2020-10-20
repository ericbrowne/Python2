# Eric Browne
#January 28th Notes Tuesday Week 4


#Collection: a data structure etc (dictionary,list,tuple,...)
#Also have the collection module!


#Built in tuple type:
tup = (1,2,3)
for v in tup:
    print(v)
print(tup[0])

from collections import namedtuple  #collections module, and lets grab 'tuple'
print("---------------------")
point = namedtuple("point","x y")
p1 = point(1,2)
print(p1[0])
print(p1.x)  # x is an alias in the tuple  p1.x == p1[0]
print(p1)
print("-----------------------------")
point = namedtuple('point',['x','y'])
point = namedtuple('point', 'x,y')
print("---------------------------")
l = ['a','b','c','a','b']
dict = {}
for letter in l:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1
print(dict)
# Super annoying to right that^^^
# So we are going to get around that with the collections module:
print("------------------------------")
from collections import defaultdict
newdict = defaultdict(int)
print(newdict['a'])
print(newdict)

from collections import OrderedDict  #organizes in order of when the keys were added
d = OrderedDict.fromkeys('acebd')
d['a']= 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
for k,v in d.items():
    print(k,v)
print(d)
print("-------------------------------")


from collections import Counter
chars = Counter("This is a string")
print(chars)
print(chars.most_common)

ints = Counter([1,2,3,4,5,5,6,44,3,3,2,5])
print(ints)
print(ints.most_common)

words = Counter("This is another string")
print(words)

print("--------------")
c = Counter('abcd')
d = Counter('sfjsdlkfj')
print( c+d)
print("----------------------------------------------------")
#More data structures:
#Stacks and Queue

#Stack = Last in first out     (Like a stack of paper)
#Queue = First in first out


#Structure that we use in python is a DEQUE = double-ended queue
from collections import deque
d = deque()
for i in range(1,10):
    d.append(i)
print(d)
#operation to remove something from a deque is called pop
for i in range(1,10):
    print(d.pop()) #they get printed in the opposite order
for i in range(1,10):  #refill the DEQUE
    d.append(i)
for i in range(1,10):
    print(d.popleft())
d.appendleft(10)
d.appendleft(11)
print(d)
print('----------------------------')
c = deque([1,2],2)
