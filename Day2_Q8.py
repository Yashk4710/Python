#WAP to find the gretest of 4 numbers entered by the user

a = int(input("enter a first number :"))
b = int(input("enter a second number :"))
c = int(input("enter a third number :"))
d = int(input("enter a fourth number : "))
if(a > b and a > c and c > d):
    print("first number is greater")

elif(b > c and b > a and b > d):
    print("second number is greater")

elif(c > d and c > b and c > a):
    print("third number is greater")

else:
    print("fourth number is greater")
