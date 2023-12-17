
def is_subsequence(s: str, t: str) -> bool:
    i1: int = 0
    i2: int = 0
    result: list = []
    while i1 < len(s) and i2 < len(t):
        if s[i1] == t[i2]:
            result.append(s[i1])
            i1 += 1
        i2 += 1
    
    print(result)
    return len(result) == len(s)

if __name__ == "__main__":
    s: str = "ace"
    t: str = "abcde"
    print(is_subsequence(s, t))