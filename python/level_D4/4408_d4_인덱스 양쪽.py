T = int(input())
for tc in range(1, T+1):
    N = int(input()) #움직이는 학생 수
    stu_move = [] #학생 도착, 출발 저장
    idx_room = [0] * 201 #복도 양쪽으로 방이 있으므로 400 / 2

    for _ in range(N): #출발 도착
        move = list(map(int, input().split()))
        #출발, 도착 방 번호 / 2해서 복도 양쪽으로 나누기
        stu_move.append(move)
        move[0] = (move[0] + 1) // 2
        move[1] = (move[1] + 1) // 2


    for i in stu_move:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0] #번호가 큰방에서 작은방으로 갈 수도있으므로 확인
        for j in range(i[0], i[1] + 1):
            idx_room[j] += 1 #idx에 더하기

    max = 0
    for m in idx_room: #큰값 찾기
        if m > max:
            max = m

    print("#{} {}".format(tc , max))
