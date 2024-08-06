#create a print a dictionary and get a output 
'''dict1 = {'brand':'Suzuki','model':'dzire','year':2012}
for x in dict1:
    print(x)
#this will print the values
dict1 = {'brand':'Suzuki','model':'dzire','year':2012}
for x in dict1:
    print(dict1[x])'''

'''dict1 = {'brand':'Suzuki','model':'dzire','year':2012}
print(dict1)
x=dict1['brand']
print(x)'''


'''d1= dict(a='Ram',b=20,c=30)
print(d1)'''


# using method
#using .len()
'''dict1 = {'brand':'Suzuki','model':'dzire','year':2012}
x= len(dict1)
print('length of the dictionary=',x)'''

#using .setdefault()

'''dict1 = {'brand':'Suzuki','model':'dzire','year':2012}
x= dict1.setdefault("place","new delhi")
print(x)''' 

#chanage the data value
'''dict1={101:'Ram',102:'shayam',103:'Kishor'}
dict1[102]='shayama'
print(dict1)'''

# using .update()
'''dict1={101:'Ram',102:'shayam',103:'Kishor'}
dict1.update({102:'Rakesh'})
print(dict1)
'''
#delete the data value and key value  .del()
'''dict1={101:'Ram',102:'shayam',103:'Kishor'}
del dict1[102]
print(dict1)'''

# using .pop() 
'''dict1={101:'Ram',102:'shayam',103:'Kishor'}
dict1.pop(103)
print(dict1)'''

# using .popitem
'''dict1={101:'Ram',102:'shayam',103:'Kishor'}
dict1.popitem()
print(dict1)'''

# using .keys()
'''dict1={101:'Ram',102:'shayam',103:'Kishor'}
x= dict1.keys()
print(x)'''

# using .values()
'''dict1={101:'Ram',102:'shayam',103:'Kishor'}
y=dict1.values()
print(dict1)'''

# using .items()
'''dict1={101:'Ram',102:'shayam',103:'Kishor'}
x = dict1.items()
print(x)'''
# AND
'''dict1={101:'Ram',102:'shayam',103:'Kishor'}
for x,y in dict1.items():
    print(x,y)'''










