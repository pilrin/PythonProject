students = [
    {"이름":"john", "국어":90, "영어": 88, "수학":99},
    {"이름":"Emily", "국어":91, "영어": 82, "수학":92},
    {"이름":"Michael", "국어":92, "영어": 84, "수학":94},
    {"이름":"Jessica", "국어":93, "영어": 89, "수학":96}
]

#테이블 헤더 출력
print("이름\t국어\t영어\t수학")
print("==============================")

#각 학생의 성적 출력
for student in students:
    name = student["이름"]
    korean = student["국어"]
    english = student["영어"]
    math = student["수학"]
    print(f"{name}\t{korean}\t{english}\t{math}")


