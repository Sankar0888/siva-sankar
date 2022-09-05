def simint(p,n,r):
    s=p*n*r/100
    return s
p=int(input("enter the principle amount => "))
n=int(input("enter the number of years => "))
if(p<=0 or n<=0):
    print("invalid input..!!!")
elif(p<n):
    print("invalid input...!!!")
else:
    cit=input("is customer senior citizen(y/n) =>").lower()
    if(cit=="y"):
        r=12
        print("your simple interest is => ",simint(p,n,r))
    elif(cit=="n"):
        r=10
        print("your simple interest is => ",simint(p,n,r))
    
    
