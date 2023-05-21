'''
튜플
   단일 변수에 여러 항목을 저장하는데 사용된다.
   순서가 있고, 변경할 수 없는 List
   둥근 괄호로 작성된다.
'''
thistuple = ('피카츄', '라이츄', '파이리')
print(thistuple)
#튜플의 길이
print(len(thistuple))

#항목 접근
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

# 튜플값 변경 방법(억지로 변경)
thistuple = ('피카츄', '라이츄', '파이리')
thiscast = list(thistuple)  # list로 casting(형변환) ['피카츄', '라이츄', '파이리']
thiscast[1] = '잠만보'         #['피카츄', '잠만보', '파이리']
thistuple = tuple(thiscast)   #('피카츄', '잠만보', '파이리')
print(thistuple)

#튜플 압축풀기
thistuple = ('피카츄', '라이츄', '파이리', '꼬북이')
(p1, p2, p3, p4) = thistuple
#ctrl + d 줄복사
#ctrl + y 줄삭제
print(p1)
print(p2)
print(p3)
print(p4)

#두개 튜플 조인 ~ + ~
thistuple1 = ('피카츄', '라이츄', '파이리', '꼬북이')
thistuple2 = ('버터풀', '야도란', '피존투', '또가스')
thistuple3 = thistuple1 + thistuple2
print(thistuple3)