n = int(input())
arr = list(map(int, input().split()))

unique_scores = list(set(arr))
unique_scores.sort()

print(unique_scores[-2])

#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem