import re
n = int(input())
pattern = r"^[7-9][0-9]{9}$"
for _ in range(n):
    phoneno = input()
    if re.match(pattern, str(phoneno)):
        print("YES")
    else:
        print("NO")
        
##https://www.hackerrank.com/challenges/validating-the-phone-number/problem