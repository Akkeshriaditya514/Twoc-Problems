def change_with_Largest_Number(Array):
    for i in range(size-1):
        Array[i] = max(Array[i+1:])
    return Array
size = int(input("Enter the number of element in the list: "))
Array = []
for i in range(size):
    Array.append(int(input("Enter the element number " + str(i+1) + " in the List: ")))
print("The new list after changing the number: ", change_with_Largest_Number(Array))