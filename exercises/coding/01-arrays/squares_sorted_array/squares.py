from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    """Returns a sorted array of the squares of the integers in nums.

    Strategy: It's a two pointers problem with an unsorted array.
    You can confront the absolute values of the integers in the array from the left and from the right.
    You can make checks between left and right in absolute value and store inside result array initialized with zeros.
    
    """
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result


def sortedSquares_pythonic(A):
    return sorted(x * x for x in A)


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))
    nums = [-7, -3, 2, 3, 11]
    print(sortedSquares(nums))
