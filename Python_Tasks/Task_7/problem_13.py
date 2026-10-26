from collections import Counter

def isValid(s):
    freq = Counter(s)
    counts = list(freq.values())
    frequency_count = Counter(counts)

    if len(frequency_count) == 1:
        return "YES"

    if len(frequency_count) == 2:
        first, second = frequency_count.keys()

        # One character appears only once; remove that character
        if (frequency_count[first] == 1 and first == 1):
            return "YES"

        # One character has a frequency one greater than the others
        if (frequency_count[second] == 1 and second - first == 1):
            return "YES"

    return "NO"


if __name__ == '__main__':
    s = input().strip()
    result = isValid(s)
    print(result)

#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem