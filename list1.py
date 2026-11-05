n = int(input("Enter number of items in the list: "))
l = []
for i in range(n):
    a = int(input("Enter item in list: "))
    l.append(a)
print("The list is: ", l)

# 1 smallest number
print("Smallest number in the list is: ", min(l))

# 2 average number
print("Average of the list is: ", sum(l) / len(l))

# 3 count occurrences of a number
count = 0
x = int(input("Enter number to count in the list: "))
for i in l:
    if i == x:
        count += 1
print("The number of the element", x, "in the list is: ", count)

# 4 reverse a list
print("The reversed list is: ", l[::-1])

# 5 sort in ascending order
for i in range(len(l)):
    for j in range(len(l) - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print("The sorted list in ascending order is: ", l)
