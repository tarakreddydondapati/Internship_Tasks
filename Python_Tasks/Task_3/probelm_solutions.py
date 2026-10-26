# # Task 3 – Python Problem Solving

# ## Q1. Find the Frequency of Each Word in a Sentence

# #**Pseudocode:**
# #1. Take a sentence as input.
# 2. Split the sentence into separate words.
# 3. Create an empty dictionary to store the words and their counts.
# 4. Go through each word and check if it is already in the dictionary.
# 5. If it is there, increase its count by one. Otherwise, add it with a count of one.
# 6. Print the dictionary.

# ## Q2. Find the Frequency of Each Character in a Word

# **Pseudocode:**
# 1. Take a word as input.
# 2. Create an empty dictionary.
# 3. Check each character in the word one by one.
# 4. If the character is already in the dictionary, increase its count.
# 5. Otherwise, add the character with a count of one.
# 6. Return the dictionary.

# ## Q3. Find the First Non-Repeating Character in a Word

# **Pseudocode:**
# 1. Take a word as input.
# 2. Count how many times each character appears.
# 3. Go through the word again from the beginning.
# 4. Check which character appears only once.
# 5. Return the first character that appears only once.
# 6. If every character repeats, return None.

# ## Q4. Check Whether Two Strings Are Anagrams

# **Pseudocode:**
# 1. Take two strings as input.
# 2. Count the frequency of each character in both strings.
# 3. Compare the two frequency dictionaries.
# 4. If both dictionaries are the same, return True.
# 5. Otherwise, return False.

# ## Q5. Find the First Repeating Character in a String

# **Pseudocode:**
# 1. Take a string as input.
# 2. Create an empty set to keep track of the characters already checked.
# 3. Read each character from left to right.
# 4. If the character is already in the set, return that character.
# 5. If it is not there, add it to the set.
# 6. If no character repeats, return None.

# ## Q6. Move All Zeros to the End of a List

# **Pseudocode:**
# 1. Take a list of numbers as input.
# 2. Create an empty list for the non-zero numbers.
# 3. Add all non-zero numbers to the new list in the same order.
# 4. Count how many zeros were in the original list.
# 5. Add that many zeros to the end of the new list.
# 6. Return the final list.

# ## Q7. Find the Second Highest Distinct Number in a List

# **Pseudocode:**
# 1. Take a list of numbers as input.
# 2. Start with two empty values for the largest and second-largest numbers.
# 3. Check each number in the list.
# 4. If a number is greater than the largest, update the largest and second-largest values.
# 5. Otherwise, check if it can become the second-largest distinct number.
# 6. Ignore duplicate values when deciding the ranks.
# 7. Return the second-largest number, or None if it does not exist.

# ## Q8. Remove Duplicates Without Changing the Original Order

# **Pseudocode:**
# 1. Take a list as input.
# 2. Create an empty list to store the unique elements.
# 3. Go through each element in the original list.
# 4. Check if the element is already in the new list.
# 5. If it is not there, add it.
# 6. Return the new list with duplicates removed.

# ## Q9. Find the Missing Number from 1 to N

# **Pseudocode:**
# 1. Take the list and the value of N as input.
# 2. Calculate the total of all numbers from 1 to N.
# 3. Find the total of the numbers in the given list.
# 4. Subtract the list total from the expected total.
# 5. Return the difference as the missing number.

# ## Q10. Find Two Numbers Whose Sum Equals a Target

# **Pseudocode:**
# 1. Take a list of numbers and a target value as input.
# 2. Start checking each number from left to right.
# 3. For each number, check the numbers that came before it.
# 4. Add the two numbers and compare their sum with the target.
# 5. If the sum matches, return the pair.
# 6. Return the first valid pair found according to the given order.
# 7. If no pair matches the target, return an empty list.

# ## Q11. Find the Number Closest to Zero

# **Pseudocode:**
# 1. Take a list of numbers as input.
# 2. Assume the first number is the closest to zero.
# 3. Check the remaining numbers one by one.
# 4. Compare how far each number is from zero.
# 5. If a number is closer, update the answer.
# 6. If two numbers are equally close, choose the positive number.
# 7. Return the final answer.

# ## Q12. Find Common Elements Between Two Lists

# **Pseudocode:**
# 1. Take two lists as input.
# 2. Create an empty list for the common elements.
# 3. Go through each element in the first list.
# 4. Check if the element is present in the second list.
# 5. If it is present and has not already been added, add it to the result.
# 6. Return the result in the same order as the first list.

# ## Q13. Rotate a List to the Right by K Positions

# **Pseudocode:**
# 1. Take a list and the number of positions K as input.
# 2. If the list is empty, return an empty list.
# 3. Adjust K based on the length of the list.
# 4. Take the last K elements from the list.
# 5. Place those elements at the beginning.
# 6. Add the remaining elements after them.
# 7. Return the rotated list.

# ## Q14. Find the Maximum Sum of Two Consecutive Elements

# **Pseudocode:**
# 1. Take a list containing at least two numbers.
# 2. Add the first two consecutive numbers and store the sum as the maximum.
# 3. Move through the list and calculate each next pair's sum.
# 4. Compare each sum with the current maximum.
# 5. If a larger sum is found, update the maximum.
# 6. Return the maximum sum.

# ## Q15. Find All Pairs of Numbers Whose Sum Equals a Target

# **Pseudocode:**
# 1. Take a list of numbers and a target value as input.
# 2. Create an empty list to store the matching pairs.
# 3. Check every possible pair using two different positions in the list.
# 4. Add the two numbers and check whether their sum equals the target.
# 5. If the sum matches, arrange the two numbers in ascending order.
# 6. Add the pair only if it is not already in the result.
# 7. Sort all the pairs based on their first number.
# 8. Return the final list of pairs.