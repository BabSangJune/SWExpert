"""
날짜 : 2021.08.15
학습 : SWEA D3
제목 : 6485. 삼성시의 버스 노선
문제 :
삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.
그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,
Bi이하인 모든 정류장만을 다니는 버스 노선이다.
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N ( 1 ≤ N ≤ 500 )이 주어진다.
다음 N개의 줄의 i번째 줄에는 두 정수 Ai, Bi ( 1 ≤ Ai ≤ Bi ≤ 5,000 )가 공백 하나로 구분되어 주어진다.
다음 줄에는 하나의 정수 P ( 1 ≤ P ≤ 500 )가 주어진다.
다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj ( 1 ≤ Cj ≤ 5,000 ) 가 주어진다.
1
2
1 3
2 5
5
1
2
3
4
5
[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 칸을 띄운 후,
한 줄에 P개의 정수를 공백 하나로 구분하여 출력한다.
j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수여야 한다.
#1 1 2 2 1 1	//첫 번째 테스트 케이스 결과
"""

T = int(input()) #tc 갯수

for tc in range(1, T+1):
    N = int(input()) #노선 갯수
    empty_lst = [[0] * 5001 for _ in range(N)] #5천개의 정류장 노선 수 만큼

    for n in range(N):
        route_start, route_end = map(int, input().split()) # n번 노선 정류장 처음과 끝

        for i in range(route_start, route_end+1):
            empty_lst[n][i] += 1 #n번 노선 다니는 정류장을 1로 바꾸기

    cp_stop = int(input()) #비교 할 노선 갯수
    result = [] #최종 값 저장
    # cnt_stop = [0] * 5001  # n번 노선이 cp_stop을 지나면 카운트 할 리스트 이거 여기있으면 초기화 안되서 중복 값이 들어가면 지랄남

    for stop in range(cp_stop): #cp_stop 만큼 no_stop input 받아오기
        cnt_stop = [0] * 5001  # n번 노선이 cp_stop을 지나면 카운트 할 리스트
        no_stop = int(input()) #비교 할 노선 번호

        for i in range(N): #노선 번호 가지고 오기
            if empty_lst[i][no_stop] == 1: #i번 노선에 no_stop이 지나가면
                cnt_stop[no_stop] += 1 # cnt_stop에 카운트

        result += [cnt_stop[no_stop]] #12개 중 5개 맞음.. 왜 ???

    # for i in range(5001): #0 제외 하고 result에 넣기 #0개 맞음 no_stop이 노선 안에 안지나가면 0 출력 해야함
    #     if cnt_stop[i] != 0:
    #         result += [cnt_stop[i]]

    print('#{}'.format(tc), end=' ')
    print(*result)