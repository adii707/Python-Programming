s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# 9.1 union
union = s1 | s2
print("The union of the two sets is: ", union)

# 9.2 intersection
intersection = s1 & s2
print("The intersection of the two sets is: ", intersection)

# 9.3 difference
d1 = s1 - s2
d2 = s2 - s1
print("The difference of the two sets is: ", d1, "and", d2)

# 10 removing duplicate values from list using set
l = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 9, 10]
s3 = set(l)
print("List after removing duplicate entries: ", s3)
