def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
n=eval(input("enter no to find factorial:"))
fact=fact(n)
print("factorial is:",fact)
