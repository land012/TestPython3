__author__ = 'xudazhou'

import re

'''
读取图片url
'''


def getimgurls(htmlline):
    imgurls = []
    pattern = re.compile(r"(http|https)://[^\"]*?(\.gif|\.png|\.jpg)")
    match = pattern.search(htmlline)
    # print("match:" + str(match))  # 必须先转成 str,才能用 + 连接
    while match:
        imgurl = match.group()
        # print(imgurl)
        imgurls.append(imgurl)
        pos = match.start()
        # print(pos)
        match = pattern.search(htmlline, pos + len(imgurl))
    return imgurls


if __name__ == "__main__":
    '''
    str1 = "embedderc=\"http://www.eaipatterns.com/img/MessageIcon1.gif\" data-image-src=\"http://www.eaipatterns.com/img/MessageIcon2.gif\" data-image-src=\"http://www.eaipatterns.com/img/MessageIcon3.png\"></span>"
    imgurls = getimgurls(str1)
    print(len(imgurls))
    for i in imgurls:
        print(i)
    '''
    '''
    imgurls2 = getimgurls("")
    print(len(imgurls2))
    '''

    '''
    str1 = "embedderc=\"http://www.eaipatterns.com/img/\" data-image-src=\"http://www.eaipatterns.com/img/MessageIcon2.gif\" data-image-src=\"http://www.eaipatterns.com/img/MessageIcon3.png\"></span>"
    imgurls = getimgurls(str1)
    for i in imgurls:
        print(i)
    '''

    str3 = "<img class=\"emoticon emoticon-smile\" " \
           "src=\"https://cwiki.apache.org/confluence/s/en_GB/5982/f2b47fb3d636c8bc9fd0b11c0ec6d0ae18646be7.1/_/images/icons/emoticons/smile.png\" " \
           "data-emoticon-name=\"smile\" alt=\"(smile)\">";
    urls = getimgurls(str3)
    print(urls)
