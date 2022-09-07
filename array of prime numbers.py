mylist = [1,2,3,4,5,66,79,81,555,123] 
print("Your List is : ", mylist) 
print("Prime numbers in your list is/are : ") 
for num in mylist: 
 # As 1 is not a prime number 
 if num > 1: 
   for i in range(2,num): 
     if (num % i) == 0: 
       break 
   else: 
     print(num)
