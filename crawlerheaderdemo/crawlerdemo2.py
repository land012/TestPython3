# coding: utf-8
"""
# Created by xudazhou at 2019/8/17
"""
import logging
import urllib.request
import urllib.error
from html.parser import HTMLParser
import socket
import time


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


def main(p_url):
    try:
        # headers = { "Cookie": "__cfduid=dc1dd57e5f5fcdf78c2dde2cae701c5d41568133605; UM_distinctid=16d1c0bdfeb0-0a0b986ac4db278-14367940-100200-16d1c0bdfec146; CNZZDATA1263093242=468847744-1568128462-%7C1568302793; jieqiVisitId=article_articleviews%3D10",
        #             "Referer": "https://www.diaosixs.org/0_10/",
        #             "Upgrade-Insecure-Requests": "1",
        #             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
        req = urllib.request.Request(p_url, headers=headers)
        # urllib.error.HTTPError: HTTP Error 502: Bad Gateway
        # urllib.error.URLError: <urlopen error _ssl.c:761: The handshake operation timed out>
        resp = urllib.request.urlopen(req, timeout=20)
        logging.info("----------------------- req fini ----------------------------- %s", resp.status)
        # socket.timeout: The read operation timed out
        res = resp.read()
    except urllib.error.HTTPError as e:
        logging.error(e)
        e_str = str(e)
        if e_str == "HTTP Error 404: Not Found":
            logging.info("-------------------------------- end")
            exit(0)
        exit(1)
    except urllib.error.URLError as e:
        logging.error(e)
        exit(1)
    except socket.timeout as e:
        logging.error(e)
        exit(1)

    logging.info("----------------------- resp read fini -----------------------------")

    html = str(res, encoding="gbk", errors="ignore")

    f = open("demo.log", mode='w', encoding='utf-8')
    f.write(html)
    f.close()

    # 每章下载到不同文件
    # myparser = MyParser(1)
    # myparser.feed(html)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    url = "https://www.diaosixs.org/1_1172/"

    start = time.time()

    main(url)

    logging.info(time.time() - start)




