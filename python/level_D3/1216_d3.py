"""
날짜 : 2021.08.17
학습 : SWEA D3
제목 : 1216. [S/W 문제해결 기본] 3일차 - 회문2
문제 :
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.
위와 같은 글자 판이 주어졌을 때, 길이가 가장 긴 회문은 붉은색 테두리로 표시된 7칸짜리 회문이다.
예시의 경우 설명을 위해 글자판의 크기가 100 x 100이 아닌 8 x 8으로 주어졌음에 주의한다.

[제약사항]
각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
글자 판은 무조건 정사각형으로 주어진다.
ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
가로, 세로 각각에 대해서 직선으로만 판단한다. 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.

[입력]
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.
#1 18
#2 17
"""
#안풀려서 참고해서 품 다시 풀어보기
for tc in range(1, 11):
    tc = int(input())
    N = 100
    result = 1 #A도 1짜리 회문이니까

    #가로줄 확인
    arr_r = []
    for _ in range(N):
        arr = input()
        arr_r.append(arr)
        for i in range(N, result, -1): #뒤에서 부터 접근
            if result > i: #result가 i보다 크면 더 실행 할 필요 없으므로 break
                break
            for j in range(N-i+1): #100 - 100 + 1 = 1, 100 - 99 + 1 = 2(0, 1)
                if arr[j:i+j] == arr[j:i+j][::-1]: #0:100, 0:99(1:100)
                    if len(arr[j:i+j]) > result:
                        result = len(arr[j:i+j])

    #세로줄 확인
    c_lst = []
    c_sub_lst = '' #문자열 만들어서
    for i in range(N):
        for j in arr_r:
            c_sub_lst += j[i]

        c_lst.append(c_sub_lst) #문자열 리스트 넣기
        c_sub_lst ='' #문자열 초기화


    for c_data in c_lst:
        for i in range(N, result, -1):
            if result > i:
                break
            for j in range(N-i+1):
                if c_data[j:i+j] == c_data[j:i+j][::-1]:
                    if len(c_data[j:i+j]) > result:
                        result = len(c_data[j:i+j])

    print('#{} {}'.format(tc, result))




