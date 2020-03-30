# coding: utf-8
"""
# Created by xudazhou at 2019/8/17
https://www.diaosixs.org
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
    list1 = [930853,930854,930855,930856,930857,930858,930859,930860,930861,930862,930863,930864,930865,930866,930867,930868,930869,930870,930871,930872,930873,930874,930875,930876,930877,930878,930879,930880,930881,930882,930883,930884,930885,930886,930887,930888,930889,930890,930891,930892,930893,930894,930895,930896,930897,956890,956891,956892,956893,956894,956895,956896,956897,956898,956899,956900,956901,956902,956903,956904,956905,956906,956907,956908,956909,956910,956911,956912,956913,956914,956915,956916,956917,956918,956919,956920,956921,956922,956923,956924,956925,956926,956927,956928,956929,956930,956931,956932,956933,956934,956935,956936,956937,956938,956939,956940,956941,956942,956943,956944,956945,956946,956947,956948,956949,956950,956951,956952,956953,956954,956955,956956,956957,956958,956959,956960,956961,956962,956963,956964,956965,956966,956967,956968,956969,956970,956971,956972,956973,956974,956975,956976,956977,956978,956979,956980,956981,956982,956983,956984,956985,956986,956987,956988,956989,956990,956991,956992,956993,956994,956995,956996,956997,956998,956999,957000,957001,957002,957003,957004,957005,957006,957007,957008,957009,957010,957011,957012,957013,957014,957015,957016,957017,957018,957019,957020,957021,979839,979840,979841,979842,979843,979844,979845,979846,979847,979848,979849,979850,979851,979852,979853,979854,979855,979856,979857,979858,979859,979860,979861,979862,979863,979864,979865,979866,979867,979868,979869,979870,979871,979872,979873,979874,979875,979876,979877,979878,979879,979880,979881,979882,979883,979884,979885,979886,979887,979888,1002727,1002728,1002729,1002730,1002731,1002732,1002733,1002734,1002735,1002736,1002737,1002738,1002739,1002740,1002741,1002742,1002743,1002744,1002745,1002746,1002747,1002748,1002749,1002750,1002751,1002752,1002753,1002754,1002755,1002756,1002757,1002758,1002759,1002760,1002761,1002762,1002763,1002764,1002765,1002766,1002767,1002768,1002769,1002770,1002771,1002772,1002773,1002774,1002892,1002893,
             1002894,1002895]

    for i in list1:
        # todo
        url = "https://www.diaosix2/%d.html" % i

        logging.info("----------------------- chapter %s" % i)

        is_try = False
        try_count = 0
        html_bytes = ""

        while try_count < 10:
            try:
                logging.info("----------------------- req start -----------------------------")
                # 需要传 User-Agent，否则返回 403
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
                req = urllib.request.Request(url, headers=headers)

                # urllib.error.HTTPError: HTTP Error 502: Bad Gateway
                # urllib.error.URLError: <urlopen error _ssl.c:761: The handshake operation timed out>
                # ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
                resp = urllib.request.urlopen(req, timeout=10)
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