#control statement
#wap  to check wiether a number is odd/even    ##
'''a=int(input("Enter number to check:"))
if a%2==0:
    print("The number is even.",a)
else:
    print("the number is odd.",a)'''


#wap to check whether an age is able to voting or not     ##
'''a =int(input("enter your age:"))
if a>=18:
    print("Eligble to vote.",a)
else:
    print("Not Eligble to vote",a)'''

#wap to find max b/w  two number                  #minimum
'''a=int(input("Enter 1st number:"));
b=int(input("Enter 2nd nuber:"));
if (a>b):
    print("Max number  A =",a)
  #  print("b is low",b);
elif b>a:
    print("Max number B =",b)
   # print("a is low",a);
else:
    print("These value are equal to A==B")'''

#wap to find max b/w three number                    #four 
'''a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3st number:"))  
if a>b and a>c:
    print("max number:",a)
elif b>a and b>c:
    print("max number:",b)
 #elif c>a and c>b:
 #print("max number:",c)
else:
    print("max number:",c)
    # print(a==b==c)'''

# wap to check whether a given number is positive , negative or zero       #
'''a = int(input("Enter the number"))
if a > 0:
    print("This is Positive number:",a)
elif a < 0:
    print("This is Negative number:",a)
else:
    print("zero")
'''


#wap to find a middle number in a group of three number
'''a = int(input("Enter 1st number="))                               
b = int(input("Enter 2st number="))
c = int(input("Enter 3st number="))
if (a>b and a<c) or (a<b and a>c):
    print("middle number:",a)
elif (b>a and b<c) or (b<a and b>c):
  print("middle number:",b)
else:
     print("middle number:",c)'''

#wap to calculate taotal marks in 5 subject (full marks=100) as well as percentage of marks and division as per the following condition
#percentage>=80-Grade-A 
#percentage>=60-Grade-B
#percentage>=40-Grade-C 
#perrcentage<40-Grade-D
'''a = int(input("Enter 1st number="))
b = int(input("Enter 2st number="))
c = int(input("Enter 3st number=")) 
d = int(input("Enter 4rth number="))
e = int(input("Enter 5rth number="))
total = a+b+c+d+e
percentage = (total/500)*100
print("total marks=",total,"Percentage=",percentage)
if percentage>=80:
    print("Grade---A")
elif percentage>=60:
    print("Grade--B")
elif percentage>=40:
    print("Grade--c")
else:
    print("Grade--D")'''


#use switch case  
# def getweek(weekday):
#     d = {
#         1: "Monday",
#         2: "Tuesday",
#         3: "Wednesday",
#         4: "Thursday",
#         5: "Friday",
#         6: "Saturday",
#         7: "Sunday"
#     }
#     return d[weekday]

# weekday = int(input("Enter1 the weekday number (1-7): "))
# print(weekday)

'''n = 30

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")'''


#wap to print a string name in revesre order with the help of list 
'''a =(input("Enter a name::::="))
l=list(a)
l.reverse()
print(l)'''


# a = "Monday"
# b= "Tuesday"
# c= "Wednesday"
# d= "Thursday"
# e= "Friday"
# f= "Saturday"
# g= "Sunday"
dy=int(input("enter the number:"))
if dy==1:
    print("monday")
elif dy==2:
    print("tuesday")
elif dy==3:
    print("Wednesday")
elif dy==4:
    print("Thursday")
elif dy==5:
    print( "Friday")
elif dy==6:
    print("Saturday")
elif dy==7:
    print("Sunday")
else:
    print("this number does not exits in weekday please try again thank you:")                   



