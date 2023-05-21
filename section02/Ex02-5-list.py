'''
list
   단일 변수에 여러 항목을 저장하는데 사용된다.
   List 항목은 순서가 지정되고 변경 가능하며 중복값을 허용
   List 에는 다양한 데이터 유형이 포함될 수 있다.
'''
thislist = ['피카츄', '라이츄', '꼬북이']
print(thislist)
print(thislist[0])

#List 길이
print(len(thislist))    #len() 함수로 리스트 길이

#List 데이터유형
list = ['피카츄', '라이츄', '파이리']
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, True]
list4 = ['abc', 34, False, 40]

#항목 접근
thislist = ['피카츄', '라이츄', '파이리']
print(thislist[1])

#변경
thislist[1] = '잠만보'
print(thislist)

#항목 변경 2개
thislist = ['피카츄', '라이츄', '파이리', '꼬북이', '버터풀', '야도란']
thislist[1:3] = ['울먹이', '메타몽']
print(thislist)

#두번째 세번쨰 값을 하나의 값으로 변경
thislist = ['피카츄', '라이츄', '파이리', '꼬북이', '버터풀', '야도란']
thislist[1:3] = ['잠만보']
print(thislist)

# 항목추가(~.append)
thislist = ["피카츄", "라이츄", "파이리"]
thislist.append("꼬부기")
print(thislist)

#항목추가 - 인덱스번호로 추가(~.insert)
thislist = ['피카츄', '라이츄', '파이리']
thislist.insert(1, '잠만보')
print(thislist)

# 항목 값으로 제거 (~.remove)
thislist = ['피카츄', '라이츄', '파이리']
thislist.remove('라이츄')
print(thislist)

# 항목을 지정된 인덱스번호로 제거(~.pop)   [pop->뽑아내다]
thislist = ['피카츄', '라이츄', '파이리']
thislist.pop(2)
print(thislist)

# 마지막 값 제거 (pop()) 괄호에 입력을 안하면 마지막 값이 없어짐
thislist = ['꼬북이', '버터풀', '야도란', '피존투']
thislist.pop()
print(thislist)

# 목록 삭제 clear()
thislist = ['피카츄', '라이츄', '파이리']
thislist.clear()
print(thislist)

# 확장
thislist = ['피카츄', '라이츄', '파이리',]
thislist.extend(['버터풀', '잠만보'])
print(thislist)

# 객체 삭제 (del)
del thislist
print(thislist)