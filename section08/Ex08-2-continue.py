'''
continue
    while문이나 for문과 같은 반복문을 강제로 건너뛰게 한다.
'''
total = 0
for a in range(1,101):
    if a % 3 == 0: # 3의 배수
        continue
    total += a
    print('a: {}, total {}'.format(a, total))

print(total)