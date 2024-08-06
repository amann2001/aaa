'''def f1():
    n=int(input("enter a number:"))
    for e in range(1,n+1):
        print(e**2,end=' ')
    print()

f1()
f1() '''

# a = "Monday"
# b= "Tuesday"
# c= "Wednesday"
# d= "Thursday"
# e= "Friday"
# f= "Saturday"
# g= "Sunday"
def f1():                                        #this is function defunations 
    dy=int(input("enter the number:"))
    if dy==1:
      print("monday")
    elif dy==2:
      print("tuesday")
    elif dy==3:
      print("Wednesday")
    elif dy==4:
      print("Thursday")                                      #take nothing return nothing
    elif dy==5:
      print( "Friday")
    elif dy==6:
      print("Saturday")
    elif dy==7:
      print("Sunday")
    else:
      print("this number does not exits in weekday please try again thank you:")

f1()# this is function call


# take something returns nothing
def add (a,b):
  c=a+b
  print("sum is ",c)

  







