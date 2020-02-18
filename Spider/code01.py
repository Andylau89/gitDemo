# 导入请求模块（python标准库）
from urllib import request

# 网址必须写完全，包括http（不是https）
url = 'http://www.sina.com.cn/'
url = 'http://www.eastmoney.com/'
url = 'http://httpbin.org/get'  #查看请求头

header = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
# 向百度发请求，得到响应对象
req = request.Request(url = url,headers = header)

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
# if '股吧互动' in str:
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
