#WAP to find the gretest of 3 numbers entered by the user

a = int(input("enter a first number :"))
b = int(input("enter a second number :"))
c = int(input("enter a third number :"))

if(a > b and a > c ):
    print("first number is greater")

elif(b > c and b > a):
    print("second number is greater")

else:
    print("third number is greater")
