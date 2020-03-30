# coding: utf-8
"""
# Created by xudazhou at 2019/8/17
https://www.yqzww.net
章节id无序
"""
import logging
import urllib.request
import urllib.error
from html.parser import HTMLParser
import socket
import ssl


logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


class MyParser(HTMLParser):

    def __init__(self):
        super(MyParser, self).__init__()
        # todo 章分隔符
        lf = open("1.log", mode="a", encoding="utf-8")
        lf.write("\n\n\n")
        lf.close()

        self.is_get = False

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
        if tag == "h1":
            self.is_get = True

        if tag == "div":
            if self.get_attr(attrs, "id") == "content":
                self.is_get = True

    def handle_endtag(self, tag):
        if self.is_get and tag == "h1":
            self.is_get = False

        if self.is_get and tag == "div":
            self.is_get = False
            # print("end %s" % tag)

    def handle_data(self, data):
        if self.is_get:
            l_data = data.strip()

            # logging.info("data %s", l_data)

            if l_data != "" and l_data is not None:
                # todo 文件名
                lf = open("1.log", mode="a", encoding="utf-8")
                lf.write(l_data)
                lf.write("\n")
                lf.close()


if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context

    # todo 每页的 id 不是从 0 或 1 自增的
    list1 = [40278091]

    for i in list1:
        # todo
        url = "https://www.yqzww.net/book_98819/%d.html" % i

        logging.info("----------------------- chapter %s" % i)

        is_try = False
        try_count = 0
        html_bytes = ""

        while try_count < 10:
            try:
                logging.info("----------------------- req start -----------------------------")
                resp = urllib.request.urlopen(url, timeout=10)
                logging.info("----------------------- req fini -----------------------------")
                html_bytes = resp.read()
                resp.close()

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
            logging.error("----------------------- http ex")
            exit(1)

        logging.info("----------------------- resp read fini -----------------------------")

        html = str(html_bytes, encoding="gbk", errors="ignore")


        myparser = MyParser()
        myparser.feed(html)

        logging.info("----------------------- parse fini -----------------------------")

    logging.info("=================================== end =====================================")