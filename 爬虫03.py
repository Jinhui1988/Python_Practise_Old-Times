# from urllib.request import urlopen
#
# url = 'http://www.baidu.com/'
# #　发送请求
# response = urlopen(url)
#
# info = response.read()
#
# # print(info.decode())
# print(response.getcode())
# print(response.geturl())
# print(response.info())


from urllib.request import urlopen
from urllib.request import Request
from wsgiref import headers

url = "http://www.baidu.com/"
user_agent
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51"

}


request = Request(url, headers=headers)
print(request.get_header('User-agent'))
response = urlopen(url)

info = response.read()

print(info.decode())


print(3+2)

print('hello      world')
print





