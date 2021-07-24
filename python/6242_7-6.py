"""
날짜 : 2021.07.14
학습 : SW Expert Academy
제목 : 6242. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 6
문제 :
다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
입력 : 입력값 없음
출력 : 1부터 100사이의 숫자 중 3의 배수의 총합: 1683
"""

student = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a, b, o, ab = 0, 0, 0, 0
for blood in student:
    if(blood=='A'):
        a+=1
    if(blood=='B'):
        b+=1
    if(blood=='O'):
        o+=1
    if(blood=='AB'):
        ab+=1

print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" % (a, o, b, ab))