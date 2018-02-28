# -*- coding:utf-8 -*-
# Write By Sunwl
# 2018/02/10
#
# 百度贴吧 静态按页抓取
# 
# python 2.7
# 运行环境 Win，Mac，Linux
# 注意：


import urllib
import urllib2


def loadPage(url,filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url:需要爬取的url地址
    """
    print ("正在下载" + filename)

    headers = {"User-Agent":"Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)"}
    request = urllib2.Request(url,headers=headers)
    return urllib2.urlopen(request).read()


def writePage(html,filename):
    """
        作用：将html内容写入本地
        html:服务器响应文件内容
    """
    print ("正在保存" + filename)
    # 文件写入
    with open(filename,"w") as f:
        f.write(html)
    print ("-" * 30)


def tiebaSpider(url,beginPage,endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url:贴吧url的前部分
        beginPage:起始页
        endPage:结束页
    """
    for page in range(beginPage,endPage + 1):
        pn = (page -1)* 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        # print (fullurl)
        html = loadPage(fullurl,filename)
        # print (html)
        writePage(html,filename)
    print ("下载完毕")


if __name__ == '__main__':
    kw = raw_input("请输入需要爬取的贴吧名:")
    beginPage = int(raw_input("请输入起始页:"))
    endPage = int(raw_input("请输入结束页:"))

    url = "http://tieba.baidu.com/f?" 
    key = urllib.urlencode({"kw":kw})
    fullurl = url + key

    tiebaSpider(fullurl,beginPage,endPage)


