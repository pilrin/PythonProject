'''
조건 연산자(삼항 연산자)
   조건식 결과에 따라 참 또는 거짓의 결과를 반환 한다.
   참 if 조건식 else 거짓
'''

a = 20
b = 100
result = (a - b) if (a >= b) else (b - a) #중간기준 참일떄 왼쪽 거짓 일때 오른쪽 실행
print('{}과 {}의 차이는 {} 입니다'.format(a, b, result))
