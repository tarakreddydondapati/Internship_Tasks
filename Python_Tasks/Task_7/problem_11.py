def twoStrings(s1, s2):
    common = set(s1) & set(s2)

    if common:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    p = int(input())

    for _ in range(p):
        s1 = input().strip()
        s2 = input().strip()

        result = twoStrings(s1, s2)
        print(result)
#https://www.hackerrank.com/challenges/two-strings/problem