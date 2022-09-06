n=eval(input("enter a number:"))
org=n
sum=0
while(n>0):
    a=n%10
    sum=sum*10+a
    n=n//10
if(sum==org):
    print("the given no is palindrome")
else:
    print("the ginen no is not a palindrome")
