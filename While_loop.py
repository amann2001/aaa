#wap to print 1 to 10
'''i=1 
while(i<=10):
    print(i)
    i=i+1'''

#wap to print 1 to n(natural number)
'''n=int(input("Enter number upto which you want to print:="))
i=0
while(i<=n):
    print(i)
    i=i+1'''

#wap to print from 10 to 1 reverse order
'''i = 10
while(i>=1):
    print(i)
    i=i-1'''

#wap a program to print only even number
'''n=int(input("Enter number upto which you want to print:="))
i=2
while(i<=n):
    print(i)
    i=i+2'''
#and
'''n=int(input("Enter number upto which you want to print:="))
i=1
while (i<=n):
    if i%2==0:
        print(i)
    i=i+1  '''

#wap to print n to 1(natural number)
'''n=int(input("Enter number upto which you want to print:="))
while(n>=1):
    print(n)
    n=n-1'''

'''n=20
while(n>=1):
    print(n)
    n=n-1'''

#wap to find sum from 1 to n
'''n=int(input("Enter number upto which you want to print:="))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
print("sum=",sum)'''

 #wap to print sum of square from 1 to n
'''n = int(input("Enter number upto which you want to print:="))
i = 1
sum=0
while(i<=n):
    sum=sum+(i*i)
    i=i+1
print("sum=",sum)'''

#wap to print sum of cubes from 1 to n
'''n = int(input("Enter number upto which you want to print:="))
i = 1
sum=0
while(i<=n):
    sum=sum+(i*i*i)
    i=i+1
print("sum=",sum)'''

#wap to print sum of factorial
'''n=5
i=1
sum=1
while(i<=n):
    sum=sum*n
    n=n-1
    print(sum)'''
    


'''n=5
i=1
t=1
while(i<=10):
    t=n*i
    print(t)
    i=i+1'''

#accesing list element via while loop
'''l1=[1,2,3,4,5]
i=5
while i>0:
    print(l1[::-1],end=' ')
    i=i-1'''

x = 'Aman Kumar'
y = list(x)

# To print 'Kumar' with a space and then 'Aman'
for k in y[-5:]:
    print(k, end='')

print(" ", end='')

for am in y[:4]:
    print(am, end='')



 

