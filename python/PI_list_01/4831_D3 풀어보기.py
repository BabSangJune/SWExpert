"""
날짜 : 2021.08.10
학습 : SWEA PI_list_01
제목 : 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스
문제 :
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는
정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고,
한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에
도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는
항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

[예시]
다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

[입력]
첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

[출력]
#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
#1 3
#2 0
#3 4
"""
# T = int(input())
#
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     charge_station = list(map(int, input().split()))
#     empty_list = []
#     tot_bus_stop = [0] * (N+1)
#     start = 0
#
#
#     for i in charge_station:
#         tot_bus_stop[i] += 1
#
#     for i in range(N+1):
#         empty_list = []
#         for j in tot_bus_stop[i+start : i+start+K]:
#             empty_list += [j]
#             start = K
#
#         print(empty_list)


#양쌤 풀이

T= int(input())

for tc in range(1, T+1):
    #K: 버스 이동 할 수 있는 거리
    #N: 마지막 종점의 위치 (0번 정류장 출발)
    #M: 충전소의 개수
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))
    bus_stop = [0] * (N+1)

    for i in charge:
        bus_stop[i] = 1

    for i in range(M):
        bus_stop[charge[i]] = 1

    bus_idx = 0 #버스의 위치
    ans = 0

    while True:
        bus_idx += K
        if bus_idx >= N: break #종점 도착 or 지나면 끝

        for i in range(bus_idx, bus_idx - K, -1):
            #if bus_stop[i] == 1:
            if bus_stop[i]:
                ans += 1
                bus_idx = i
                break

        else:
            ans = 0
            break

    print('#{} {}'.format(tc, ans))


