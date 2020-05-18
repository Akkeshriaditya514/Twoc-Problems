num = int(input("Enter the Number:"))
for i in range(num):
	x=' '*i+'*'+' '*(num-i-1)
	print(x+x[::-1])
for i in range(num):
	x=' '*(num-i-1)+'*'+' '*i
	print(x+x[::-1])