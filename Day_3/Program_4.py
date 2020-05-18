# List is taken by me , as not given in question
ints_list = [1, 2, 3, 4, 3, 2, 5, 6, 3]
for x in ints_list:
    if ints_list.count(x) > 1:
        ints_list.remove(x)
print(ints_list)