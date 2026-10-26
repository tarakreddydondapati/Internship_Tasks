t = int(input())
u = set(list(map(int, input().split(' '))))
v = int(input())
w = set(list(map(int, input().split(' '))))
print(len(list(u.intersection(w))))


##https://www.hackerrank.com/challenges/py-set-intersection-operation/problem