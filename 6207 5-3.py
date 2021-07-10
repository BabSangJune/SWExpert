"""
날짜 : 2021.07.11
학습 : SW Expert Academy
제목 : 6207. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 5. 연산자 3
문제 : 섭씨(℃)를 화씨(℉)로 변환하는 프로그램을 작성하십시오.
이 때 물의 빙점은 화씨 32도이고 비등점은 화씨 212도(표준 기압에서)입니다.
물의 비등점과 빙점 사이에 정확하게 180도 차이가 납니다.
그러므로 화씨 눈금에서의 간격은 물의 빙점과 비등점 사이의 간격의 1/180입니다.
입력 : 28 출력 : 28.00 ℃ =>  82.40 ℉
"""

a = float(input())

print("{0:.2f} ℃ =>  {1:.2f} ℉".format(a , a*1.8+32))
#섭씨의 빙점 0 화씨의 빙점 32 물의 비등점 100 화씨 비등점 212 섭씨 빙점 비등점 180도 차이 화씨 빙점 비등점 1/180
#a/100*180+32