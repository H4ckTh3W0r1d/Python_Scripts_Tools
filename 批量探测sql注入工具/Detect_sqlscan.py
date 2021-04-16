#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup
header={
'Host': 'cn.bing.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
'Connection': 'keep-alive',
'Cookie': 'DUP=Q=mVtmYzuzKF1E4RGEp16GAw2&T=390299413&A=2&IG=BB1A24E20BB247DEA60F691BEC646E34; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7B6F1AAE454B48CFB7194BD3E8F9F9C1&dmnchg=1; SRCHUSR=DOB=20200505&T=1589451212000; _EDGE_V=1; MUID=02684545ACC26CA438B94B84ADEC6DD8; MUIDB=02684545ACC26CA438B94B84ADEC6DD8; SRCHHPGUSR=CW=1920&CH=543&DPR=1&UTC=480&HV=1589451219&WTS=63725048012&NEWWND=1&NRSLT=-1&SRCHLANG=&AS=1&NNT=1&HAP=0; _SS=SID=16FE2359541468FE10782D93553A690C&bIm=SFG; _EDGE_S=mkt=zh-cn&SID=16FE2359541468FE10782D93553A690C; ipv6=hit=1589454816360&t=4; ENSEARCH=BENVER=0; _FP=hta=on; ULC=P=C8DC|1:1&H=C8DC|1:1&T=C8DC|1:1',
'Upgrade-Insecure-Requests': '1',
'Cache-Control': 'max-age=0',
'TE': 'Trailers'
}
header2={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36 Edg/81.0.416.58'
}
huixian = "on line"
    
def main(url):
    #定义爬取页数
    for i in range(0,871,10):
        urlc = url+str(i)
        r = requests.get(url=urlc,headers=header)
        soup = BeautifulSoup(r.text,'html.parser')
        #lxml需要安装，不然解析不出来。速度比html.parser快[pip install lxml]
        #soup = BeautifulSoup(r.text,'lxml')
        urls = soup.find_all(name='a',target="_blank",attrs={'class':None,'id':None})
        #取到网站地址
        for a in urls:
            try:
                #判断url中是否存在'='号
                if '=' in a['href']:
                    #构造payload
                    payload= a['href']+'%27'
                    rr = requests.get(url=payload,headers=header2,timeout = 1)
                    #判断关键字是否在返回的数据中
                    if huixian in str(rr.content):
                        print(a['href'])
                        #判断结果是否已经保存在文件中，如果不存在，把url保存在文件中
                        result = open('result.html', 'a+')
                        with open('result.html') as f:
                            if rr.url not in f.read():
                                result.write('<a href="' + rr.url + '" target="_blank">' + rr.url + '</a>')
                                result.write('\r\n</br>')
                                result.close()
            except:
                pass
if __name__ == '__main__':
    if len(sys.argv) == 2:
        key = sys.argv[1]
    else:
        print("Tips：python3 Detect_sqlscan.py <key>")
    try:
        #构造url
        urla = 'https://cn.bing.com/search?q='
        urlb = '&first='
        url =  urla + str(key) + urlb
        main(url)
    except:
        pass
