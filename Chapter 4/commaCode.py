def commaAnd(list1):
    return ", ".join(list1[:-1]) + " and " + list1[-1]

numItems = int(input())
userlist = []
for i in range(numItems):
    userlist.append(str(input()))

print(commaAnd(userlist))
