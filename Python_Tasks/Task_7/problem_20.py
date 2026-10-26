def superReducedString(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if len(stack) == 0:
        return "Empty String"

    return "".join(stack)


if __name__ == '__main__':
    s = input().strip()
    result = superReducedString(s)
    print(result)
#https://www.hackerrank.com/challenges/reduced-string/problem