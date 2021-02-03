def solve(test_case):
    if test_case[1] == 0:
        if test_case[0] % 2 == 0:
            return 0
        else:
            return 1
    else:
        return abs(test_case[1] - test_case[0])


n = int(input())
cases = []
for index in range(n):
    pos = list(map(int, input().split()))
    res = solve(pos)
    cases.append(res)

for i in range(len(cases)):
    print(cases[i])