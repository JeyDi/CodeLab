# Arrays and strings

Exercises related to Arrays and strings

## 1. Palindrome

Given a string `s`, return `true` if it is a palindrome, `false` otherwise.

A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: `abcdcba` or `racecar`

## 2. Ordered sum

Given two sorted integer arrays `arr1` and `arr2`, return a new array that combines bot of them and is also sorted.

In this example you can use the two pointers scrolling index.

Reflect when you want to perform the sorting.

## 3. Is subsequence

Given two strings `s` and `t` , return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters. For example: `"ace"` is a subsequence of `"abcde"` while `"aec"` is not

## 4. Reverse string

Write a function that reverses a string. The input string is given as an array of characters `s`.
You must do this by modifying the input array **in-place** with $$O(1)$$ extra memory.

Some constraint:

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ascii character

### Example 4.1

```python
# input
s: list = ["h", "e", "l", "l", "o"]
# output
["o", "l", "l", "e", "h"]
```

### Example 4.2

```python
# input
s: list = ["H", "a", "n", "n", "a", "h"]

#output
["h", "a", "n", "n", "a", "H"]
```

## 5. Squares of a sorted array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order

### Example 5.1

```text
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]
```

### Example 5.2

```text
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

**Constraints:**

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.

