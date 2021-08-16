"""
날짜 : 2021.08.12
학습 : SWEA D3
제목 : 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
문제 :
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )
3
3 6
5 15
5 10\
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#1 1
#2 1
#3 0
"""

T = int(input())
for tc in range(1, T+1):
    nums = list(range(1, 13)) # 1~12까지 숫자 리스트
    ele_len, tot_num = map(int, input().split()) #입력값 원소 길이, 합
    result_cnt = 0 #결과 저장할곳
    N = len(nums) #nums의 길이

    for i in range(1 << N):
        ele_cnt = 0
        ele_hap = 0

        for j in range(N):
            if i & (1 << j): #이까지 부분집합 만들기
                ele_cnt += 1 #부분집합 갯수당 하나씩 누적
                ele_hap += nums[j] #부분집합 합계

        #밖으로 나와서 입력값과 위 if에서 저장한 값들 둘다 같으면
        if ele_len == ele_cnt and ele_hap == tot_num:
            result_cnt += 1 #하나씩 누적

    print('#{} {}'.format(tc, result_cnt))




