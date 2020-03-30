import urllib
import urllib.request
import os

__author__ = 'xudazhou'

'''
图片下载
'''


def imagedown(imgurl, localpath):
    """
    使用 imgurl 中的文件名 作为 本地保存的文件名
    优化点：
        可以加入 localpath 是否存在，是否是文件夹的判断逻辑
        超时处理
        本地文件是否存在
    :param imgurl:
    :param localpath:
    :return:
    """
    try:
        imgname = imgurl[imgurl.rfind("/")+1:]
        # print(imgname)
        filepath = localpath + os.path.sep + imgname
        if not os.path.exists(filepath):
            resp = urllib.request.urlopen(imgurl, data=None, timeout=10)
            data = resp.read()
            file1 = open(filepath, "wb")
            file1.write(data)
            file1.close()
    except Exception as ex:
        print("down image exception %s" % imgurl)
        file2 = open("E:\\TDDOWNLOAD\\failed.txt", "a")
        file2.write(imgurl + "\n")
        file2.close()
        # raise ex


# 这个相当于 java 里的 main方法
# 应该主要用于编写功能模块时，自测使用
if __name__ == "__main__":
    # imagedown("https://www.baidu.com/img/bd_logo1.png", "E:\\TDDOWNLOAD\\images\\")
    # imagedown("http://www.enterpriseintegrationpatterns.com/img/ChannelIcon.gif", "E:\\TDDOWNLOAD\\images\\")

    imagedown("http://www.enterpriseintegrationpatterns.com/img/MessageChannelSolution.gif", "E:\\TDDOWNLOAD\\")
    imagedown("http://www.enterpriseintegrationpatterns.com/img/MessageChannelSolution.gif", "E:\\TDDOWNLOAD\\")
