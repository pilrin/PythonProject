'''
divomde() 함수
    두 숫자를 인자로 전달 받아
    첫번째 인자를 두번째 인자로
    나눈 몫과 나머지를 tuple 형식으로 변환
'''
money = 10000
reice = 3000
result = divmod(money, reice)
print('빵을 {}개 사고 {}원이 남았습니다.'
      .format(result[0], result[1]))