def linear_search(arr,x):
    size = len(arr)
    for i in range(size):
        if arr[i] == x:
            return i
    return -1 #찾고자 하는 값이 없는 경우

# 실행코드
arr = [1, 3, 5, 7, 8]
print(linear_search(arr, 5))