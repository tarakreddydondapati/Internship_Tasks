n = int(input())
set1 = set(map(int, input().split()))
b = int(input())
set2 = set(map(int, input().split()))

set3 = set1.union(set2)
num = 0
for i in set3:
    num += 1

print(num)

##https://www.hackerrank.com/challenges/py-set-union/problem