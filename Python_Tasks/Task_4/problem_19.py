from collections import Counter

x = int(input())
shoe_sizes = list(map(int, input().split()))

shoe_inventory = Counter(shoe_sizes)

n = int(input())
total_money = 0

for _ in range(n):
    size, price = map(int, input().split())

    if shoe_inventory[size] > 0:
        total_money += price
        shoe_inventory[size] -= 1

print(total_money)

#https://www.hackerrank.com/challenges/collections-counter/problem