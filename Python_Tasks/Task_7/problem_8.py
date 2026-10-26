def gemstones(arr):
    common_minerals = set(arr[0])

    for rock in arr[1:]:
        common_minerals = common_minerals.intersection(set(rock))

    return len(common_minerals)


if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(input().strip())

    result = gemstones(arr)
    print(result)

#https://www.hackerrank.com/challenges/gem-stones/problemSS