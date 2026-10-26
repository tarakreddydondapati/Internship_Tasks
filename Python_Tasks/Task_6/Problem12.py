n = int(input())
s = set(map(int, input().split()))
c = int(input())
for _ in range(c):
    cmd, *args = input().split()
    getattr(s, cmd)(*map(int, args))
print(sum(s))

##https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem