'''
O(2^n)
    지수 시간 복잡도, 피보나치 수열처럼 재귀적 알고리즘
'''
'''
(fibonacci(3)) -> 1 + 1 = 2ㄴ
    1번
    fibonacci(2) 1 + 0
            1번
            fibonacci(1) -> 1
            2번
            fibonacci(0) -> 0
            
    2번
    fibonacci(1) ->
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) +   fibonacci(n-2)

print(fibonacci(40))
