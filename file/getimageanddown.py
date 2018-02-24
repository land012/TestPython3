import com.demo.redemo.redemoimgurl
import com.demo.url.imagedown
import traceback
import locale

__author__ = 'xudazhou'
'''
读取 html 中的图片 url，并下载到本地
'''

print(locale.getpreferredencoding(False))  # cp936

file1 = open("E:\TDDOWNLOAD\camel-manual-2.18.0.html", "r", encoding="utf-8")
line = ""
i = 0

try:
    for line in file1:
        i += 1
        imgurls = com.demo.redemo.redemoimgurl.getimgurls(line)
        if len(imgurls) > 0:
            for imgurl in imgurls:
                print(imgurl)
                # 替换域名
                imgurl = imgurl.replace("www.eaipatterns.com", "www.enterpriseintegrationpatterns.com")
                com.demo.url.imagedown.imagedown(imgurl, "E:\\TDDOWNLOAD\\images\\")
except Exception:
    traceback.print_exc()
    print("i=%d" % i)
    print("exception line:%s" % line)
file1.close()
