'''
21.
다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.
'''
# scores = [88,30,61,55,95]
# for i in range(1,6):
#     if scores[i-1] >= 60:
#         print("{}번 학생은 {}점으로 합격입니다.".format(i,scores[i-1]))
#     else:
#         print("{}번 학생은 {}점으로 불합격입니다.".format(i,scores[i-1]))    

'''
22.
1부터 100까지의 숫자를 for 문과 range 함수를 이용해 출력하십시오.
'''
# for i in range(1,101):
#     print(i)

'''
23.
1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.

output> 2 4 6 8 ... 98 100
'''
# num = ""
# for i in range(1,101):
#     if i%2==0:
#         num += str(i)+" "
# print(num)


'''
24.
1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.

output> 1, 3, 5, 7, 9, ... 95, 97, 99
'''
# num = ""
# for i in range(1,101):
#     if i%2!=0:
#         num += str(i)+", "
# print(num[:-2])

'''
25.
1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.

output> 1부터 100사이의 숫자 중 3의 배수의 총합: 1683
'''
# total=0
# for i in range(1,101):
#     if i%3==0:
#         total += i
# print("1부터 100사이의 숫자 중 3의 배수의 총합: {}".format(total))

'''
26.
다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

output> {'A': 3, 'O': 3, 'B': 2, 'AB': 2}
'''
# bdata = ['A','A','A','O','B','B','O','AB','AB','O']
# bdic = {'A':0,'O':0,'B':0,'AB':0}
# for b in bdata:
#     if b=='A':
#         bdic['A'] +=1
#     elif b=='O':
#         bdic['O'] +=1
#     elif b=='B':
#         bdic['B'] +=1
#     elif b=='AB':
#         bdic['AB'] +=1
# print(bdic)

'''
27.
다음은 학생의 점수를 나타내는 리스트입니다.
[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.

output> 454
'''
# slst = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# i=0
# count = 0
# total = 0
# while count<9:
#     if slst[i]<80:
#         slst.pop(i)
#     else:
#         i +=1
#     count += 1
# for s in slst:
#     total += s
# print(total)

'''
28.
while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

*****
****
***
**
*
'''
# i=0
# while i<5:
#     print('*'*(5-i))
#     i += 1


'''
29.
while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

*******
 *****
  ***
   *
'''
# fail
# i=0
# while i<5:
#     print("{:^7}".format('*'*(7-2*i)))
#     i += 1

# i=0
# while i<4:
#     print("{}{}".format(" "*i,'*'*(7-2*i)))
#     i += 1

'''
30.
다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.

input> 11
output>
0 1 2 3 4 5 6 7 8 9
0 2 0 0 0 0 0 0 0 0
'''
# N = input()
# Ndic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
# for i in range(len(N)):
#     if int(N[i]) == 0:
#         Ndic[0] += 1
#     elif int(N[i]) == 1:
#         Ndic[1] += 1
#     elif int(N[i]) == 2:
#         Ndic[2] += 1
#     elif int(N[i]) == 3:
#         Ndic[3] += 1
#     elif int(N[i]) == 4:
#         Ndic[4] += 1
#     elif int(N[i]) == 5:
#         Ndic[5] += 1
#     elif int(N[i]) == 6:
#         Ndic[6] += 1
# k=""
# v=""
# for key in Ndic.keys():
#     k += str(key)+" "
# for value in Ndic.values():
#     v += str(value)+" "
# print(k)
# print(v)

'''
31.
for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

    *
   **
  ***
 ****
*****
'''
# for i in range(1,6):
#     print("{:>5}".format("*"*i))

'''
32.
다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.

input>9
output>1001
'''
# ten = int(input())
# b = format(ten, '#b')
# print(b[2:])

'''while문으로 10진수에서 2진수 변환하는 함수 만들기!!!!'''