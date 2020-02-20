# 导入请求模块（python标准库）
from urllib import request

# 网址必须写完全，包括http（不是https）
url = 'http://www.baidu.com/'
# url = 'http://www.eastmoney.com/'
# url = 'http://httpbin.org/get'  #查看请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# 向百度发请求，得到响应对象
req = request.Request(url = url,headers = headers)

response = request.urlopen(req)
# print(response)
# print(type(response))
# 获取相应对象内容（网页源代码）
# print(response.read())
# 返回结果为b开头，是byte类型的
# print(response.read())
str = response.read().decode('utf-8')

print(str)


# print(len(str))
# if '百度一下' in str:
#     print('yes')

#
# print(response.getcode())
# print(response.geturl())
#
# byte = response.read()
# # byte = b'input\n'
# print(byte)
# print(len(byte))
# str = bytes.decode(byte)
# print(str)

# import urllib.request


# with urllib.request.urlopen('http://www.baidu.com/') as f:
#     print(f.read().decode('utf-8'))



# print(a)
# string=str(b,'utf-8')
# print(string)
