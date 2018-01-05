#!/usr/python3
import re
import urllib.request
import chardet

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()

    #根据你传进来的参数自动辨别编码格式，然后进行相应的解码
    encode_type = chardet.detect(html)
    html = html.decode(encode_type['encoding'])

    #手动转码
    #html=html.decode('UTF-8')

    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)"'
    img=re.compile(reg)

    imglist=re.findall(img,html)
    i = 0
    for imgurl in imglist:

        #写法一
        #f = open(r"D:/1234/" + str(i) + '.jpg', 'wb')
        #req = urllib.request.urlopen(imgurl)
        #buf = req.read()
        #f.write(buf)
        #i += 1

        #写法二
        urllib.request.urlretrieve(imgurl, 'D:/1/%s.png' % i)
        i += 1

html=getHtml("http://tieba.baidu.com/p/2125112048#!/l/p1")
print(html)