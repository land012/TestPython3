# coding: utf-8
"""
# Created by xudazhou at 2019/8/17
爬 66buke
"""
import logging
import urllib.request
import urllib.error
from html.parser import HTMLParser
import socket


logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

class MyParser(HTMLParser):

    def __init__(self, f_name):
        super(MyParser, self).__init__()
        self.isbt = False
        self.booktext = ""
        self.i = 0
        self.novel_end = False
        self.f_name = f_name

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for e in attrs:
                if e[0] == "id":
                    if e[1] == "BookText":
                        self.isbt = True
        if self.isbt:
            # print("start %s" % tag)
            if tag == "div":
                self.i += 1
            if tag == "p":
                for e in attrs:
                    if e[0] == "class":
                        if e[1] == "preload":
                            self.novel_end = True

    def handle_endtag(self, tag):
        if self.isbt and tag == "div":
            # print("end %s" % tag)
            if self.i > 0:
                self.i -= 1
                if self.i == 0:
                    self.isbt = False
                    # print("is_novel_end %s" % self.novel_end)

            # print("i %s" % self.i)

    def handle_data(self, data):
        if self.isbt:
            l_data = data.strip()
            if l_data != "" and l_data is not None:
                self.booktext += l_data
                lf = open("%s.txt" % self.f_name, mode="a", encoding="utf-8")
                lf.write(l_data)
                lf.write("\r\n")
                lf.close()

    def is_chapter_end(self):
        return self.booktext == ""

    def is_novel_end(self):
        return self.novel_end



if __name__ == "__main__":
    i = 0
    is_novel_end = False

    while True and not is_novel_end:
        j = 0

        while True:
            url_pre = "https://www.66buke.com/book/7816/"
            if j == 0:
                url = url_pre + "%s.html" % i
            else:
                url = url_pre + "%s_%s.html" % (i, j)

            logging.info("chapter %s page %s" % (i, j))

            is_try = False
            try_count = 0
            res = ""

            while try_count < 3:
                try:
                    # urllib.error.HTTPError: HTTP Error 502: Bad Gateway
                    # urllib.error.URLError: <urlopen error _ssl.c:761: The handshake operation timed out>
                    resp = urllib.request.urlopen(url, timeout=20)
                    logging.info("----------------------- req fini -----------------------------")
                    # socket.timeout: The read operation timed out
                    res = resp.read()
                    is_try = False
                except urllib.error.HTTPError as e:
                    logging.error(e)
                    is_try = True
                    try_count += 1
                except urllib.error.URLError as e:
                    logging.error(e)
                    is_try = True
                    try_count += 1
                except socket.timeout as e:
                    logging.error(e)
                    is_try = True
                    try_count += 1

                if not is_try:
                    break

            if is_try:
                logging.error("http ex")
                exit(1)

            logging.info("----------------------- resp read fini -----------------------------")

            html = str(res, encoding="utf-8", errors="ignore")

            # f = open("1.txt", mode='w', encoding='utf-8')
            # f.write(html)
            # f.close()

            # 每章下载到不同文件
            myparser = MyParser(1)
            myparser.feed(html)
            if myparser.is_chapter_end() or myparser.is_novel_end():
                logging.info("----------------------- chapter fini -----------------------------")
                is_novel_end = myparser.is_novel_end()
                break

            logging.info("----------------------- parse fini -----------------------------")

            j += 1

        i += 1
        # if i == 3:
        #     break




