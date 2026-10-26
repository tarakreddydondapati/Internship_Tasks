def weightedUniformStrings(s, queries):
    weights = set()
    previous_char = ""
    current_weight = 0

    for char in s:
        weight = ord(char) - ord('a') + 1

        if char == previous_char:
            current_weight += weight
        else:
            current_weight = weight

        weights.add(current_weight)
        previous_char = char

    result = []

    for query in queries:
        if query in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result


if __name__ == '__main__':
    s = input().strip()
    n = int(input())

    queries = []

    for _ in range(n):
        queries.append(int(input()))

    result = weightedUniformStrings(s, queries)

    for answer in result:
        print(answer)
#https://www.hackerrank.com/challenges/weighted-uniform-string/problemS