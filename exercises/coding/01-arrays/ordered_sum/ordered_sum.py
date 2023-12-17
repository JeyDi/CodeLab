def ordered_sum(arr1: list, arr2: list) -> list:
    p1: int = 0
    p2: int = 0
    result = []
    
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1
    
    while p1 < len(arr1):
        result.append(arr1[p1])
        p1 += 1
    
    while p2 < len(arr2):
        result.append(arr2[p2])
        p2 += 1
    
    return result


if __name__ == "__main__":
    # The arrays must be already sorted before.
    arr1 = [2, 4,7,10,20]
    arr2 = [0, 1, 6, 11]
    result = ordered_sum(arr1, arr2)
    print(result)