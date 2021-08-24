"""
날짜 : 2021.08.17
학습 : SWEA D2
제목 : 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교
문제 :
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
ABC
ZZZZZABCZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.

ABC
ZZZZAZBCZZZZZ
문자열이 일치하지 않으므로 0을 출력.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#1 1
#2 0
#3 1
"""

T = int(input()) #tc 갯수

for tc in range(1, T+1):
    fst_str = input()
    snd_str = input()
    cnt = 0 #결과

    len_str = len(fst_str) #첫 문자 길이
    for i in range(len(snd_str) - len_str + 1):
        if fst_str == snd_str[i:i+len_str]:
            cnt += 1

    print('#{} {}'.format(tc, cnt))

