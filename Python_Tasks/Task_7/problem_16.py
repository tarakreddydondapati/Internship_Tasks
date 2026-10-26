def caesarCipher(s, k):
    result = ""

    k = k % 26

    for char in s:
        if char.islower():
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result += new_char

        elif char.isupper():
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result += new_char

        else:
            result += char

    return result


if __name__ == '__main__':
    n = int(input())
    s = input()
    k = int(input())

    result = caesarCipher(s, k)
    print(result)
#https://www.hackerrank.com/challenges/caesar-cipher-1/problem