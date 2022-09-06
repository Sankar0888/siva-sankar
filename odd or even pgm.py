try:
    n=int(input("Enter the number:"))
    if n>=0:
        if n%2==0:
            print("The number is even")
        else:
            print("The number is odd")
    else:
        print("Enter only positive number")
except:
    print("Invalid")
