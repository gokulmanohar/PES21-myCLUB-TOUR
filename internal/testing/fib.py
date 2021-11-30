n = int(input())
a = 0
b = 1
print("0")
for i in range(n):
    c = a+b
    a = b
    b = c
    print(c)