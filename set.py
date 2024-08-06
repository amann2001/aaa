'''s1={1,2,4,3,5}
print(type(s1))
print(s1)'''

'''x={1,30,11,20,30,10,2,3,4}
print(x)'''

#list cantained duplicate value in a container then useing  of set remove duplicate value 
'''l1=[1,2,3,1,2,3,40,50,40,60,60,70,80,70,60,50,1,2,3,4]
print(len(l1))
x=l1.count(1)
print(x)
l1=list(set(l1))
print(l1)'''
# set can be access own element only using for loop and  you can access one element that is used to another way convert to list than acess one by one element 
#s1={1,2,3,1,2,3,40,50,40,60,60,70,80,70,60,50,1,2,3,4}
# for x in s1:
#     print(x,end=' ')

'''l1=list(set(s1))
print(l1)
print(l1[4])
print(sorted(s1))'''

# all method of set
# add() method 
# a={1,2,4} 
# b={1,2,3,4,5} 
# a.add((12))
# print(a)
# #update()
# a.update((12,23,34))
# print(a)
# remove
# a.remove(4)
# print(a)
# #discard()
# a.discard(6)
# print(a)
# # pop()
# a.pop()
# print(a)
# # clear()
# a.clear()
# print(a)
# # intersection()
# x = a.intersection(b)
# print(x) 
# union()
# x= a.union(b)
# print(x)
a={1,2,3,4,5} 
b={1,2,3,4,5} 
# # issubset()
# x = a.issubset(b)
# print(x)                             # same element in variable name of set function 
# issuperset
x = a.issuperset(b)
print(x)


