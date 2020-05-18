def duplicate(s):
    output=""
    for i in s:
        if i not in output:
            output+=i
    return (output)

s = input("Enter the String:")
print("String after removing the duplicates is:",duplicate(s))