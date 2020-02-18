# 导入请求模块（python标准库）
import urllib.request

# 网址必须写完全，包括http（不是https）
url = 'http://www.baidu.com/'
timeout = 3

# 向百度发请求，得到响应对象
response = urllib.request.urlopen(url)
# print(response)
# print(type(response))
# 获取相应对象内容（网页源代码）
# print(response.read())
# 返回结果为b开头，是byte类型的
print(response.read())

print(response.getcode())
print(response.geturl())

print(response.read().decode('utf-8'))

# string=str(b,'utf-8')
# print(string)
