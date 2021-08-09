"""
날짜 : 2021.07.08
학습 : SW Expert Academy
제목 : 6196. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 4. 변수
문제 : 1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.
입력 : 9 출력 : 11106
"""

# 1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.

a = int(input()) # 입력
s = 0 # 배수 계산
total = 0 # 합 계산

for i in range(1,5): # 1~4 반복
    s = s*10 + 1 # 1, 11, 111, 1111
    total += a*s # a + aa + aaa + aaaa

print(total)


'''
간단하게 
a = int(input())
print(1234 * a)

가능
'''