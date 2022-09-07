n=int(input("enter any number"))
if(n==0 or n==1):
    print(n,"number is neither prime or comoposite")
elif n>1:
    for i in range (2,n):
        if(n%i==0):
           print(n,"composite number")
        break
    else:
        print(n,"prime number")
else:
        print("please enter postive number only")
          
  
