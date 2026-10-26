
# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    frequency = {}

    for word in sentence.split():
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    frequency = {}

    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


# Q3. Find the First Non-Repeating Character
def first_non_repeating(word):
    frequency = character_frequency(word)

    for char in word:
        if frequency[char] == 1:
            return char

    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return character_frequency(s1) == character_frequency(s2)


# Q5. Find the First Repeating Character
def first_repeating(string):
    seen = set()

    for char in string:
        if char in seen:
            return char
        seen.add(char)

    return None


# Q6. Move All Zeros to the End
def move_zeros(nums):
    result = []

    for num in nums:
        if num != 0:
            result.append(num)

    zero_count = len(nums) - len(result)

    for i in range(zero_count):
        result.append(0)

    return result


# Q7. Find the Second Highest Distinct Number
def second_highest(nums):
    largest = None
    second = None

    for num in nums:
        if largest is None or num > largest:
            if num != largest:
                second = largest
                largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second


# Q8. Remove Duplicates While Preserving Order
def remove_duplicates(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    return result


# Q9. Find the Missing Number from 1 to N
def missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


# Q10. Find the First Pair Whose Sum Equals Target
def two_sum(nums, target):
    seen = set()

    for num in nums:
        needed = target - num

        if needed in seen:
            # Find the earliest previous occurrence
            for previous in nums[:nums.index(num)]:
                if previous == needed:
                    return [needed, num]

        seen.add(num)

    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    if not nums:
        return None

    result = nums[0]

    for num in nums[1:]:
        if abs(num) < abs(result):
            result = num
        elif abs(num) == abs(result) and num > result:
            result = num

    return result


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if not nums:
        return []

    k = k % len(nums)

    return nums[-k:] + nums[:-k] if k != 0 else nums[:]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    largest_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > largest_sum:
            largest_sum = current_sum

    return largest_sum


# Q15. Find All Unique Pairs Whose Sum Equals Target
def all_pairs(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])

                if pair not in result:
                    result.append(pair)

    result.sort(key=lambda pair: pair[0])

    return result
