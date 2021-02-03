def is_palindrome(string):
    return string == string[::-1]

mirrorable = 'AHIMOTUVWXY'
flag = True
name = input()

for letter in name:
    if letter not in mirrorable:
        flag = False

if (flag and is_palindrome(name) and len(name) != 1) or (len(name) == 1 and flag):
    print("YES")
else:
    print("NO")