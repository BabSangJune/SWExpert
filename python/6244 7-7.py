"""
날짜 : 2021.07.14
학습 : SW Expert Academy
제목 : 6244. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 7
문제 :
다음은 학생의 점수를 나타내는 리스트입니다.
[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
입력 : 입력값 없음
출력 : 454
"""

score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum=0

while(score):
    x = score.pop()
    if(x>=80):
        sum += x

print(sum)