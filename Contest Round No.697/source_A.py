n = int(input())
cases = []
for i in range(n):
    case = int(input())
    cases.append(case)

res = []
for index in range(len(cases)):
    if cases[index] == 2:
        res.append(False)
    for divisor in range(2, cases[index]):
        if cases[index] % 2 != 0:
            res.append(True)
            break
        else:
            res.append(False)
            break

for result in range(len(res)):
    if res[result]:
        print("YES")
    else:
        print("NO")
