
from solutions import (
    word_frequency,
    character_frequency,
    first_non_repeating,
    are_anagrams,
    first_repeating,
    move_zeros,
    second_highest,
    remove_duplicates,
    missing_number,
    two_sum,
    closest_to_zero,
    common_elements,
    rotate_right,
    max_consecutive_sum,
    all_pairs
)

# Q1. Word Frequency
print("Q1:", word_frequency("python is easy and python is powerful"))
print("Q1 Extra:", word_frequency("hello hello world"))

# Q2. Character Frequency
print("Q2:", character_frequency("banana"))
print("Q2 Extra:", character_frequency("apple"))

# Q3. First Non-Repeating Character
print("Q3:", first_non_repeating("swiss"))
print("Q3 Extra:", first_non_repeating("aabbc"))

# Q4. Anagrams
print("Q4:", are_anagrams("listen", "silent"))
print("Q4 Extra:", are_anagrams("hello", "world"))

# Q5. First Repeating Character
print("Q5:", first_repeating("programming"))
print("Q5 Extra:", first_repeating("abcdef"))

# Q6. Move Zeros to End
print("Q6:", move_zeros([0, 3, 0, 1, 2, 0, 4]))
print("Q6 Extra:", move_zeros([0, 1, 0, 2]))

# Q7. Second Highest Distinct Number
print("Q7:", second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 Extra:", second_highest([5, 5, 3]))

# Q8. Remove Duplicates
print("Q8:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 Extra:", remove_duplicates([1, 1, 2, 3, 2]))

# Q9. Missing Number
print("Q9:", missing_number([1, 2, 4, 5, 6], 6))
print("Q9 Extra:", missing_number([1, 3, 4, 5], 5))

# Q10. Two Sum
print("Q10:", two_sum([2, 7, 11, 15], 9))
print("Q10 Extra:", two_sum([1, 4, 2, 3], 5))

# Q11. Closest to Zero
print("Q11:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 Extra:", closest_to_zero([-4, 4, 6]))

# Q12. Common Elements
print("Q12:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 Extra:", common_elements([2, 2, 3, 4], [2, 4]))

# Q13. Rotate Right
print("Q13:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 Extra:", rotate_right([10, 20, 30], 1))

# Q14. Maximum Consecutive Sum
print("Q14:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 Extra:", max_consecutive_sum([-5, -2, -8]))

# Q15. All Unique Pairs
print("Q15:", all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 Extra:", all_pairs([1, 2, 3, 4], 5))
