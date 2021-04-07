list1 = [1, 4, 6, 8, 7]
n = len(list1)
x = list1[n - 1]
for i in range(n - 1, 0, -1):
    list1[i] = list1[i - 1]
list1[0] = x
for i in range(n):
    print(list1[i], end=' ')