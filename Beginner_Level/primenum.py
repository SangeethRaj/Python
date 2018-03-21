n = int(input("Enter a number: "))  
  
if n > 1:  
   for i in range(2,n):  
       if (n % i) == 0:  
           print(n,"NO")  
           print(i,"times",n//i,"is",n)  
           break  
   else:  
       print(n,"YES")  
         
else:  
   print(n,"NO")  
