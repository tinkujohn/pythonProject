#lists and tuples and sets

a = 10
b =10
# mem location of a and b

print(id(a))

l1 = [ 1 ,5 ,6, 10]
l1.sort(reverse = True)
print(l1)

#list functions
print( max(l1))
l1.append('hello')
print(l1)

'''
tuple -> immutable list, we cannot add elements or modify the elements
list elements cannot be used as key in dictionary, only immutable type can be used
int, string, tuple are immutable
list is mutable
'''

coordinates = { (0,0) : 100, (1,1) : 200}
coordinates[(1,0)] = 150
coordinates[(0,1)] = 125

t1 = ( 1,2,3)
print(t1)
print(type(t1))

print(t1.count(2))
print(t1.index(3))

'''
sets do not allow duplicates
No order
cannot use slicing/indexing
set doesnot guarantee order
set is mutable -> set.upadte([]) and set.remove()
cannot perform repetition using * operator
'''

s1 = { 'a', 'ab', 3}
print(type(s1), s1)

'''
fs = frozenset(s1)
Frozen set -> takes set and converts
immutable
'''

'''
Range type
always start from 0 to max-1
'''

r1 =range(5)
print(type(r1))

#feature a added here