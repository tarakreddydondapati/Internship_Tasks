def stringConstruction(s):
    unique_chars = set(s)
    return len(unique_chars)


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input().strip()
        print(stringConstruction(s))

#https://www.hackerrank.com/challenges/string-construction/problem