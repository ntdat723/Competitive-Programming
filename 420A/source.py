n, k = map(int, input().split())
path = list(map(int, input().split()))

longest = 1
temp_longest = 1
previous = path[0]
if len(path) == 2 and path[0] != path[1]:
    longest = 2
else:
    for step in range(1, n):
        if path[step] != previous:
            temp_longest += 1
        else:
            if temp_longest > longest:
                longest = temp_longest
            temp_longest = 1
        previous = path[step]
        if temp_longest > longest:
            longest = temp_longest

print(longest)
