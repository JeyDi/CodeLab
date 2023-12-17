def check_palindrome(word: str) -> bool:
    left: int = 0
    right: int = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


string_1 = "racecar"
string_2 = "hello"
string_3 = "abcdcba"

if __name__ == "__main__":
    print(check_palindrome(string_1))
    print(check_palindrome(string_2))
    print(check_palindrome(string_3))