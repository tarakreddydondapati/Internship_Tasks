def rangoli(size):
    import string

    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        right = alphabet[size - i - 1:size]
        letters = left + right
        row = "-".join(letters)
        lines.append(row.center(4 * size - 3, "-"))

    for i in range(size - 2, -1, -1):
        lines.append(lines[i])

    return "\n".join(lines)





if __name__ == '__main__':
    n = int(input())
   
#https://www.hackerrank.com/challenges/alphabet-rangoli/problemS