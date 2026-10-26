
from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))

    top = float('inf')
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            cube = blocks.popleft()
        else:
            cube = blocks.pop()

        if cube <= top:
            top = cube
        else:
            possible = False
            break

    print("Yes" if possible else "No")
#https://www.hackerrank.com/challenges/piling-up/problem