def countoccur(A, x): 
   c = 0
   for i in A: 
      if (i == x): 
         c = c + 1
   return c 
A=list()
n1=int(input("Enter the size of the List ::"))
print("Enter the Element of List ::")
for i in range(int(n1)):
   k=int(input(""))
   A.append(k)
n=int(input("Enter an element to count number of occurrences ::"))       
print("Number of Occurrences of ",n,"is",countoccur(A, n)) 