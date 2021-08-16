"""
날짜 : 2021.08.10
학습 : SWEA PI_list_01
제목 : 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max
문제 :
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

[입력]
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#1 630739
#2 740510
#3 838110
"""

def My_max_num(nums):
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

def My_min_num(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num


T = int(input())

for tc in range(1, T+1):
    cnt_nums = int(input())
    list_nums = list(map(int, input().split()))

    result = My_max_num(list_nums) - My_min_num(list_nums)
    print('#{} {}'.format(tc, result))

