num = int(input("Enter the number:"))
for i in range(num):
    x = ((str(num - i) + "*") * (num-i) + str(num - i))
    print(x[:-1])
for i in range(2,num+1):
    y = ((str(i) + "*") * (i) + str(i+1))
    print(y[:-1])