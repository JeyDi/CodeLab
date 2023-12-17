from typing import List


def reverse_string(s: List[str]) -> List[str]:
    """Reverses the order of the characters in the list.

    Strategy: It's a two pointers problem with an input list.
    You need to swap the characters using a starting pointer and an ending pointer with a temporary variable.
    """
    left = 0
    right = len(s) - 1
    temporary = ""

    while left < right:
        temporary = s[left]
        s[left] = s[right]
        s[right] = temporary
        left += 1
        right -= 1

    return s


def reverse_string_beautiful(s: List[str]) -> List[str]:
    """Reverses the order of the characters in the list.

    Beautiful compact solution.
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1


def reverse_string_recursive(s: List[str]) -> List[str]:
    """Reverses the order of the characters in the list.

    Using a recursive strategy.
    """

    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

    helper(0, len(s) - 1)


def reverse_string_short(s: List[str]) -> List[str]:
    """Reverses the order of the characters in the list.

    Made in the easy pythonic way :)
    """
    return s.reverse()
    # return s[::-1]


if __name__ == "__main__":
    s: List[str] = ["h", "e", "l", "l", "o"]
    print(reverse_string(s))
    s: List[str] = ["H", "a", "n", "n", "a", "h"]
    print(reverse_string(s))
