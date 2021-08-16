"""
날짜 : 2021.08.10
학습 : SWEA PI_list_01
제목 : 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max
문제 :
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )
3
5
49679
5
08271
10
7797946543

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
#1 9 2
#2 8 1
#3 7 3
"""

T = int(input())

for tc in range(1, T+1):
    cnt_cards = int(input()) #카드 몇개
    list_cards = list(input()) #카드 숫자
    empty_list = [0] * 10 #숫자 카운트할 리스트
    max_num = 0 #가장 큰 숫자 저장용
    max_num_cnt = 0 #카운트 저장 용


    for i in list_cards:
        #카드숫자가 empty_list의 해당 인덱스에 +1씩 누적
        empty_list[int(i)] += 1 

    #카운트 한 카드숫자와 갯수 가져오기
    for idx_card, num_card in enumerate(empty_list):
        if max_num_cnt <= num_card: #가장 많은 카드가져오기
            max_num_cnt = num_card
            max_num = idx_card

    print('#{} {} {}'.format(tc, max_num, max_num_cnt))

