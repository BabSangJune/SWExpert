'''
34.
다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
input> eye
output> eye
입력하신 단어는 회문(Palindrome)입니다.
'''
# # string[::-1] 문자열 반대로 뒤집기
# # “”.join(reverse(string)) 문자열 반대로 뒤집기

# word = input()
#
# def check(w):
#     rew=w[::-1]
#
#     if word == rew:
#         print(rew)
#         print("입력하신 단어는 회문(Palindrome)입니다.")
#     else:
#         print("입력하신 단어는 회문(Palindrome)이 아닙니다.")
#
# check(word)


'''
35.
다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.
input> 홍길동
이순신
가위
바위
output> 바위가 이겼습니다!
'''
# def rsp(a,b):
#     if a == "바위":
#         if b == "가위":
#             print("바위가 이겼습니다!")
#         elif b == "보":
#             print("보가 이겼습니다!")
#         else : print("비겼습니다!")
#     elif a == "가위":
#         if b == "바위":
#             print("바위가 이겼습니다!")
#         elif b == "보":
#             print("가위가 이겼습니다!")
#         else : print("비겼습니다!")
#     elif a == "보":
#         if b == "바위":
#             print("보가 이겼습니다!")
#         elif b == "가위":
#             print("가위가 이겼습니다!")
#         else : print("비겼습니다!")
#
# playera = input()
# playerb = input()
# rspa = input()
# rspb = input()
# rsp(rspa,rspb)

'''
36.
소수를 검사하는 함수를 정의하고, 다음의 결과와 같이 사용자가 입력한 숫자가
소수인지를 판단하는 프로그램을 작성하십시오.
소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력
input> 13
output> 소수입니다.
'''

# def primenum(num):
#     cnt = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             cnt += 1
#     if cnt == 2:
#         print("소수입니다.")
#     else:
#         print("소수가 아닙니다.")
# num = int(input())
# primenum(num)

'''
37.
다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.
input> 10
output> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''

# def fibonacci(n):
#     flst = []
#     for i in range(n):
#         if i<2:
#             flst.append(1)
#         else:
#             fnum = flst[i-2]+flst[i-1]
#             flst.append(fnum)
#     print(flst)
#
# fibonacci(int(input()))

'''
38.
리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고
이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.
output>
[1, 2, 3, 4, 3, 2, 1]
[1, 2, 3, 4]
'''

# lst = [1, 2, 3, 4, 3, 2, 1]
#
# def unilst(lst):
#     nlst = list(set(lst))
#     print(lst)
#     print(nlst)
#
# unilst(lst)
#
# # 내꺼는 아니지만 인터넷 참고 global활용
# li = [1, 2, 3, 4, 3, 2, 1]
#
# unique_list = list()
# def unique_value(li):
#     global unique_list
#     for i in range(len(li)):
#         num = li[i]
#         if num not in unique_list:
#             unique_list.append(num)
#
# print(li)
# unique_value(li)
# print(unique_list)

'''
39.
정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.
output>
[2, 4, 6, 8, 10]
5 => False
10 => True
'''

# def inout(n, lst):
#     if n in lst:
#         print("{} => True".format(n))
#     else : print("{} => False".format(n))
#
# lst = [2, 4, 6, 8, 10]
# print(lst)
# inout(5, lst)
# inout(10, lst)

'''
40.
다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한
팩토리얼 값을 구하는 프로그램을 작성하십시오.
'''

# def fac(num):
#     fnum = 1
#     for i in range(1,num+1):
#         fnum *= i
#     print(fnum)
#     # return fnum
#
# fac(5)

'''
41.
숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면
정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.
'''
# def numsquare(num):
#     print("square({}) => {}".format(num, num**2))
#
# num1, num2 = map(int, input().split(','))
#
# numsquare(num1)
# numsquare(num2)

'''
42.
인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고
결과를 출력하는 프로그램을 작성하십시오.
'''

# def whatslong(a, b):
#     if len(a) > len(b):
#         print(a)
#     elif len(a) < len(b):
#         print(b)
#     else : print("길이가 같습니다.")
#
# a, b = input().split(", ")
# whatslong(a, b)

'''
43.
인자로 전달된 숫자를 이용해 카운트다운하는 함수 countdown을 정의하고,
이 함수를 이용하여 countdown(0), countdown(10)을 순서대로 실행하십시오.
0보다 작거나 같은 인자가 전달되었을 경우 "카운트다운을 하려면 0보다 큰 입력이 필요합니다."를 출력하십시오.
'''

# def countdown(n):
#     if n <= 0:
#         print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
#     else:
#         for i in range(n, 0, -1):
#             print(i)
#
# countdown(0)
# countdown(10)
