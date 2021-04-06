l = [2, 7, 5]
base = []
lists = [base]
for i in range(len(l)):
    original = lists[:]
    new = l[i]
    for j in range(len(lists)):
        lists[j] = lists[j] + [new]
    lists = original + lists
print(lists)