l = int(input())
for i in range(0, l):
    m = int(input())
    n = list(map(int, input().split()))
    o = int(input())
    p = list(map(int, input().split()))
    if set(n).issubset(set(p)):
        print(True)
    else:
        print(False)
        
##https://www.hackerrank.com/challenges/py-check-subset/problem