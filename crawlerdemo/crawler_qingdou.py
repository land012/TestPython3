# coding: utf-8
"""
# Created by xudazhou at 2019/8/17
http://www.qdtxt.cc
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

    def __init__(self):
        super(MyParser, self).__init__()
        # todo 章分隔符
        lf = open("1.txt", mode="a", encoding="utf-8")
        lf.write("\n\n################################################################################\n\n")
        lf.close()

        self.is_get = False
        self.novel_end = False
        self.start_tag = ""
        self.f_name = ""

    @staticmethod
    def get_attr(p_list, p_key):
        """

        :param p_list: [(k1, v1), (k2, v2)]
        :param p_key:
        :return:
        """
        for l_e in p_list:
            if l_e[0] == p_key:
                return l_e[1]

        return None

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.start_tag = tag
            self.is_get = True

        if tag == "div":
            if self.get_attr(attrs, "id") == "chapter_content":
                self.is_get = True

    def handle_endtag(self, tag):
        if self.is_get and tag == "title":
            self.start_tag = ""
            self.is_get = False

        if self.is_get and tag == "div":
            self.is_get = False
            # print("end %s" % tag)

    def handle_data(self, data):
        if self.is_get:
            l_data = data.strip()

            # logging.info("data %s", l_data)

            if l_data == "DedeCMS提示信息":
                logging.info("----------------------------------- is_novel_end -----------------------------------")
                self.novel_end = True

            if self.start_tag == "title":
                self.f_name = l_data.split("_")[0]

            if l_data != "" and l_data is not None:
                # todo 文件名
                lf = open("1.txt", mode="a", encoding="utf-8")
                lf.write(l_data)
                lf.write("\n")
                lf.close()

    def is_novel_end(self):
        return self.novel_end


if __name__ == "__main__":
    i = 120

    while True:
        # todo
        chapter_id = 996480
        url = "http://www.er_%d_%d.html" % (chapter_id, i)

        logging.info("----------------------- chapter %s" % i)

        is_try = False
        try_count = 0
        html_bytes = ""

        while try_count < 10:
            try:
                logging.info("----------------------- req start -----------------------------")
                # urllib.error.HTTPError: HTTP Error 502: Bad Gateway
                # urllib.error.URLError: <urlopen error _ssl.c:761: The handshake operation timed out>
                resp = urllib.request.urlopen(url, timeout=10)
                logging.info("----------------------- req fini -----------------------------")
                # socket.timeout: The read operation timed out
                html_bytes = resp.read()
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

        html = str(html_bytes, encoding="utf-8", errors="ignore")

        # f = open("1.txt", mode='w', encoding='utf-8')
        # f.write(html)
        # f.close()

        myparser = MyParser()
        myparser.feed(html)
        if myparser.is_novel_end():
            # logging.info("is_novel_end")
            exit(0)

        logging.info("----------------------- parse fini -----------------------------")

        i += 1
