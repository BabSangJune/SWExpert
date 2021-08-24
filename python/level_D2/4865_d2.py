"""
날짜 : 2021.08.17
학습 : SWEA D2
제목 : 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수
문제 :
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
파이썬의 경우 딕셔너리를 이용할 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#1 2
#2 1
#3 3
"""

T = int(input()) #tc 갯수

for tc in range(1, T+1):
    fst_str = input()
    snd_str = input()

    lst_cnt = []
    for i in range(len(fst_str)):
        cnt = 0
        for j in range(len(snd_str)):
            if fst_str[i] == snd_str[j]: #첫 문자열과 두번째 문자열 하나씩 비교
                cnt += 1 #카운트
        lst_cnt += [cnt] #리스트에 넣기

    max_num = 0
    for i in lst_cnt: #제일 큰값 뽑기
        if max_num < i:
            max_num = i

    print('#{} {}'.format(tc, max_num))






