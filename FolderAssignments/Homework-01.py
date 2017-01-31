``` python
"""
Name: Erika Price
Email: eprice1988@yahoo.com 
Assignment: Homework 1 - Lists and Dictionaries
Due: 31 Jan 2017 @ 11:00 a.m.
"""

print('Problem: A')
"A"
a = [1, 5, 4, 2, 3]
print(a[0], a[-1])
#Prints: 1, 3

a[4] = a[2] + a[-2]
print(a)
#Prints: [1, 5, 4, 2, 6]
#does the addition on a[2](4) + a[-2](2) which is 6 and
#replaces a[4] with that value

print(len(a))
#Prints: 5
#The number of items in the list, how long the list is.

print(4 in a)
#Print: True
#looks for the number 4 in the list. 
#If it is there it returns true otherwise false

a[1] = [a[1], a[0]]
print(a)
#Prints: [1,[5, 1], 4, 2, 6]
#Replaces a[1] (which is 5) with both a[1] and a[0] printing 
print('')

print('Problem: B')
"B"
list = [3, 1, 2, 1, 5, 1, 1, 7]
#removes all instances of 1 from the list.
def remove_all(x, list):
    for i in list:
        list.remove(x)

remove_all(1,list)
print(list)
print('')


print('Problem C: ')
"C"
list = [1, 2, 4, 2, 1]
#adds y to the end of the list the number of times x occurs in list.
def add_this_many(x, y, List):
    for i in list:
        if i == 1:
            list.append(y)
add_this_many(1, 5, list)
print(list)
print('')

print('Problem D:')
"D"

a = [3,1,4,2,5,3]
print(a[:4])
#Prints: [3,1,4,2] (prints a[0] up to but not including a[4])

print(a)
#Prints: [3, 1, 4, 2, 5, 3] all of list a

print(a[1::2])
#Prints: [1, 2, 3] (every other element in the list)

print(a[:])
#Prints: [3, 1, 4, 2, 5, 3] (prints the entire list)

print(a[4:2])
#Prints: []

print(a[1:-2])
#Prints: [1, 4, 2] (prints everything from a[1] up to but not including a[-2](second to last a[]))

print(a[::-1])
#Print: [3, 5, 2, 4, 1, 3] Prints the list backwards! yay!
print('')

print('Problem E: ')
"E"
b = [3, 2, 4, 5, 1]
def reverse(lst):
    size = len(lst)
    hiindex = size - 1
    its = size // 2
    for i in xrange(0, its):
        temp = lst[hiindex]
        lst[hiindex] = lst[i]
        lst[i] = temp
        hiindex -= 1
print('Initial list: ') 
print(b)
print('')
reverse(b)
print(b)
print('')

print('Problem F: ')
"F"
a = [1, 2, 3, 4, 5]
newlist=[]
#Return a new list, with the same elements of lst, rotated to the right k.
def rotate(lst, k):
   rotated_lst = []
   for i in range(len(lst)):
       rotated_lst.append(lst[(i-k)% len(lst)])
   return rotated_lst
   
print('Initial list without rotation:')
print(a)
print('List with rotation:')
print rotate(a, 3)
print('')

print('Problem H: ')
"H"
superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}
print(superbowls['tom brady'])
# Prints: 3

superbowls['peyton manning'] = 1
print(superbowls)
# Prints: {'peyton manning': 1, 'tom brady': 3, 'joe flacco': 0, 'joe montana': 4}

superbowls['joe flacco'] = 1
print(superbowls)
# Prints:{'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

print('colin kaepernick' in superbowls)
#Prints: False (searched for colin Kaepernick and found no instance of such)

print(len(superbowls))
#Prints: 4 (gives the length of the dictionary, how many entries)

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False (checking to see if those two are equal )

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {'joe flacco': 1, ('eli manning', 'giants'): 2, 'joe montana': 4, 'peyton manning': 1, 'tom brady': 3}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {3: 'cat', 'peyton manning': 1, ('eli manning', 'giants'): 2, 'joe flacco': 1, 'joe montana': 4, 'tom brady': 3}

superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {3: 'cat', 'peyton manning': 1, ('eli manning', 'giants'): 5, 'joe flacco': 1, 'joe montana': 4, 'tom brady': 3}

#superbowls[['steelers', '49ers']] = 11
print(superbowls)
"""
Prints: Traceback (most recent call last):
File "Homework-01.py", line 162, in <module>
superbowls[['steelers', '49ers']] = 11
TypeError: unhashable type: 'list'
"""
#fix would be superbowls[('steelers', '49ers')] = 11
print('')

print('Problem I:')
"I"
d = {1:{2:3, 3:4}, 2:{4:4, 5:3}}
def replace_all(d, x, y):
    for k in d.keys():
        if type(d[k]) is dict:
            replace_all(d[k], x, y)
        elif d[k] is x:
            d[k] = y 

print(d)
replace_all(d, 3, 1)
print(d)
print()

print('Problem J')
"J"
d = {1:2, 2:3, 3:2, 4:3}
def rm(d,x):
    for k,v in d.items():
            if v == x:
                del d[k]

print(d)
rm(d,2)
print(d)
```
