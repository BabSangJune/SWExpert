'''
6232.
다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
'''
# word = input()
# if word == word[::-1]:
#     print(word)
#     print("입력하신 단어는 회문(Palindrome)입니다.")
# else: pass

'''
6239.
다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.
'''
# print(" ".join(input().split(" ")[::-1]))

'''
6241.
다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로
구분하는 프로그램을 작성하십시오.
'''
# url = input()
# protocol = url[:url.find('://')]
# host = url[url.find('://')+3:url.rfind('/')]
# others = url[url.rfind('/')+1:]
# print("protocol: {}\nhost: {}\nothers: {}".format(protocol,host,others))

# # my code
# url = "http://www.example.com/test?p=1&q=2".split('/')
# print("protocol: {}\nhost: {}\nothers: {}".format(url[0][:4],url[2],url[3]))

'''
6678.
다음의 결과와 같이 여러 문장을 입력받아 대문자로 변환해 출력하는 프로그램을 작성합니다.
아무 것도 입력하지 않고 엔터만 입력하면 입력이 종료됩니다.
'''
# # Runtime error
# while True:
#     sen = input()
#     if sen == "":
#         break
#     print(">> {}".format(sen.upper()))

# # not my code //EOFError(End Of File)
# while True:
#     try:
#         print(">> {}".format(input().upper()))
#     except EOFError:
#         break

'''
6243.
사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고,
중복된 단어없이 단어를 콤마(,)로 구분해 사전순으로 출력하는 프로그램을 작성하십시오.
'''
# word = ",".join(sorted(list(set(input().split(" ")))))
# print(word)

'''
6248.
다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오.
'''
# a = input()
# sen=""
# for i in range(len(a)):
#     if i%2==0:
#         sen += (a[i])
# print(sen)

# # not mine
# raw_str = list(input())
# for i in range(0, len(raw_str), 2):
#     print(''.join(raw_str[i]), end='')
