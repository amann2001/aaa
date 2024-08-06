#using for when looping a know number of times

'''for i in [1,2,3,4]:
    print(i)

(
for i in ["yash"]:
    print(i)


for i in (1,2,3,4):
    print(i)    

for i in ("yash"):
    print(i) 
    '''

# a sequence is an ordered collection of objects

'''for ch in ["Aksh"]:
    print(ch)
    print(type(ch))
   
for ch in ["1,2,3,4"]:
    print(ch)
    
for ch in ("Aksh"):
    print(ch)
    print(type(ch))
'''

# iterating a specifie number of times

'''for i in range(5):
    print('hii')'''


# loop find 5th position number
'''a = [1,2,3,4,5,6,7]
for index in range (len(a)):
    if index == 5:
        print("the 5th position number is :",a[index])'''

#Dynamic iterating 
#Grade A->=90
#Grade B ->=60
#Grade c ->=27

'''name = ("kishor","puneet","Abs")
marks = 90,60,27
for result in marks:
    if result >=90:
        print("Grade A","PASS")
    elif result >=60:
        print("Grade B","PASS")
    else:
        print("Grade A", "FAIL") '''
#table on n(natural value)
'''x=int(input("Enter number to find table:"))
for y in range(1,11):
    print(x, "x", y, "=", x * y)'''

#####

''''for weekday in range(1):
    weekday = int(input("enter the weekdays number 1-7==:"))
    if weekday ==1:
        print("IT IS Monday")
    elif  weekday ==2:
       print("IT IS Tuesday")
    elif weekday ==3:
       print("IT IS Wednesday")
    elif  weekday ==4:
       print("It is Thursday")
    elif weekday ==5:
       print("It is Friday")
    elif weekday ==6:
       print("It is Saturday")
    elif weekday ==7:
       print("It is Sunday")
    else:
       print("IT IS NOT A valid weekday number")
       print("THANKS>>>>>>>>>>>>>>")'''
#Exit the loop when x is "banana"
'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break'''

#Exit the loop when x is "banana", but this time the break comes before the print:

'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)'''
    

#accesing list element via for loop
'''l1=[2,3,1,5,6]
i= len(l1)
# for x in l1[1]
# print(l1[1],end=' ')
# for x in l1[5::-2]:print(x,end=' ')
# for x in li(6,-1,-1):print(x,end=' ')
for x in l1[i::-1]:
    print(x,end=' ')'''

'''x='Aman Kumar'
Name=''
cnt=0
y=list(x)
lnth=len(y)
lenth1=lnth
for nm in y [lnth::-1]:
    Name+=nm
    cnt+1
    if cnt==lenth1:print(Name)'''

#x='Aman Kumar'
'''y=list(x)
print(y)
for am in y[-5::]:
    print(am,end='')
print(" ",end='')
for k in y[:4]:
    print(k,end='')'''

x=('Aman kumar')
# y=x[::-1]
y=x[0::]
z=tuple(y)
print(z)
    




    
