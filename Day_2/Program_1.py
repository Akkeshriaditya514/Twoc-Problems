#Check number is Odd or Even

def is_Odd_Or_Even(num):
	if num%2==0:
		print("Number is EVEN number")
	else:
		print("Number is ODD number")

#Check numberis a Prime number

def is_Prime(num):
    count=0
    for i in range(2,num//2):
        if num%i==0:
            count+=1
    if count==0:
        print("Number is a Prime number")
    else:
        print("Number is not a Prime number")

#Check number is a Palindrome number

def is_Palindrome(num):
    l = str(num)
    if l==l[::-1]:
        print("Number is a Palindrome number")
    else:
        print("Number is not a Palindrome number")
        
#Check number is an Armstrong number

def is_Armstrong(num):
    l = str(num)
    x = 0
    for i in l:
        x += int(i)**3
    if x==num:
        print("Number is an Armstrong number")
    else:
        print("Nuber is not an Armstrong number")
		
num = int(input("Enter the Number:"))

is_Odd_Or_Even(num)

is_Prime(num)

is_Palindrome(num)

is_Armstrong(num)