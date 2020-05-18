x = list(input('Enter elements of a list x:').split())
y = list(input('Enter elements of a list y:').split())

print('List 1: ',x)
print('List 2: ',y)
print('Intersection : ',list(set(x).intersection(set(y))))