t1 = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9)
print("The first tuple is: ", t1)
print("The second tuple is: ", t2)
# 6 common of two lists
common = set(t1) & set(t2)
print("The common elements in the two tuples are: ", common)
# 7 list to tuple
l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
t3 = tuple(l)
print("The third tuple converted from list is: ", t3)
# 8 tuple to list
t4 = (11, 12, 13, 14, 15)
l2 = list(t4)
print("The list converted from tuple is: ", l2)
