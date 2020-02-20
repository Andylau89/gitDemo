# 导入请求模块（python标准库）
from urllib import request
# 导入编码模块
from urllib import parse

# 网址必须写完全，包括http（不是https）
url = 'http://www.eastmoney.com/'
# url = 'https://www.baidu.com/s?wd=%E7%BE%8E%E6%99%AF'
url = 'https://www.baidu.com/s?'
url = 'http://www.sina.com.cn/'

url = 'https://www.sogou.com/web?'

# url = 'http://cn.bing.com/search?'
# url = 'http://httpbin.org/get'  # 查看请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

# keyword = input("请输入查询内容：")
########################编码，拼接完整URL##############################
dir_query = {'query': '刘德华', 'page': '1'}
query_str = parse.urlencode(dir_query)
print('URL编码为：', query_str)

url = url + query_str

print('拼接后的网址为：', url)
########################编码，拼接完整URL##############################
#
req = request.Request(url=url, headers=headers)
response = request.urlopen(req)
html_str = response.read().decode('utf-8')
# print(html_str)

# print(len(str))
# https://cn.bing.com/search?q=%E5%88%98%E5%BE%B7%E5%8D%8E&first=31

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
#
if '成龙默契足' in html_str:
    print('yes')

filename = '{}.html'.format('Andylau')
# 编码改为utf-8后，保存的html可以打开。编码如果默认，或者gbk打开后是乱码
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html_str)

# 对中文进行编码
print("中国：", parse.quote("中国"))
print("中国：", parse.quote("中"))
print("中国：", parse.quote("国"))
print("中国：", parse.quote("中央"))

url = 'http://www.baidu.com/s?wd={}'
word = input("输入要搜素的内容：")

query_string = parse.quote(word)
print(url.format(query_string))

print(parse.unquote('%E4%B8%AD%E5%9B%BD'))