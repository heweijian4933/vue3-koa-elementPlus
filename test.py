#coding:utf-8
# print('xixi')
import requests 
#这是书籍的地址
book_url='http://www.xbiquge.la/10/10489/'

#通过requests库的get方法向小说目录地址发送请求，即让requests这个人去book_url这个地址取货
response_1=requests.get(book_url)

#设定编码，因为网址用 utf-8 编码，不然会导致中文显示乱码
#通俗地说那就是requests这个人与仓库语言不同，沟通有障碍，所以通过 encoding这个方法来同化沟通语言
response_1.encoding='utf-8'

#输出货物部分信息
print(response_1.text)