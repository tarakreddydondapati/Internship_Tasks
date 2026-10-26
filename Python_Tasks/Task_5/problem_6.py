def average(arr):
    distinct_heights = set(arr)
    return sum(distinct_heights) / len(distinct_heights)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#https://www.hackerrank.com/challenges/py-introduction-to-sets/problemS