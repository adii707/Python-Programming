n = int(input("Enter a number: "))
print("Multiplication table upto 10 for ", n, "is: ")
for i in range(1, 11):
    print(n, "X", i, "=", n * i)
