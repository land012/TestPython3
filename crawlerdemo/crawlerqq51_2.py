# coding: utf-8
"""
# Created by xudazhou at 2019/8/17
https://www.qq51.org
章节id无序
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
        # lf = open("1.txt", mode="a", encoding="utf-8")
        # lf.write("\n\n################################################################################\n\n")
        # lf.close()

        self.is_get = False
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
        if tag == "li":
            if self.get_attr(attrs, "class") == "active":
                self.is_get = True

        if tag == "div":
            if self.get_attr(attrs, "class") == "panel-body content-body content-ext":
                self.is_get = True

    def handle_endtag(self, tag):
        if self.is_get and tag == "li":
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
                lf = open("1.txt", mode="a", encoding="utf-8")
                lf.write(l_data)
                lf.write("\n")
                lf.close()


if __name__ == "__main__":
    # todo 每页的 id 不是从 0 或 1 自增的
    list1 = [312304,312305,312307,312308,312310,312312,312314,312315,312317,312319,312320,312321,312323,312324,312326,312327,312329,312330,312332,312333,312335,312336,312338,312339,312341,312343,312344,312346,312348,312349,312351,312352,312354,312356,312358,312359,312361,312363,312364,312365,312367,312369,312370,312372,312373,312375,312376,312378,312380,312382,312383,312384,312386,312387,312389,312390,312392,312394,312395,312397,312399,312400,312402,312404,312405,312407,312409,312410,312412,312414,312415,312417,312418,312420,312421,312423,312425,312426,312428,312429,312431,312433,312435,312436,312438,312439,312450,312451,312452,312454,312455,312457,312458,312459,312461,312462,312463,312464,312465,312467,312468,]

    for i in list1:
        # todo
        url = "https://www.qq51.org/9/9435/%d.html" % i

        logging.info("----------------------- chapter %s" % i)

        is_try = False
        try_count = 0
        html_bytes = ""

        while try_count < 10:
            try:
                logging.info("----------------------- req start -----------------------------")
                # urllib.error.HTTPError: HTTP Error 502: Bad Gateway
                # urllib.error.URLError: <urlopen error _ssl.c:761: The handshake operation timed out>
                # ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
                resp = urllib.request.urlopen(url, timeout=10)
                logging.info("----------------------- req fini -----------------------------")
                # socket.timeout: The read operation timed out
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