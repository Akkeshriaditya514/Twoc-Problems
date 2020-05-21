di=dict()
di_new=dict()
for _ in range(int(input('Enter the Number of values you want:'))):
	key = input('Enter The key : ')
	value = int(input('Enter the value: '))
	di[key]=value
	if value not in di_new.values():
		di_new[key]=value

print('Update dictionary :',di_new)