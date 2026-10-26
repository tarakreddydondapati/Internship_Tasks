def makingAnagrams(s1, s2):
    deletions = 0

    for char in "abcdefghijklmnopqrstuvwxyz":
        count1 = s1.count(char)
        count2 = s2.count(char)

        deletions += abs(count1 - count2)

    return deletions


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()

    result = makingAnagrams(s1, s2)
    print(result)
#https://www.hackerrank.com/challenges/making-anagrams/problemS