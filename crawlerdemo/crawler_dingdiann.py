# coding: utf-8
"""
# Created by xudazhou at 2019/8/17
https://www.dingdiann.com
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
    list1 = [7292871,7292872,7292873,7292874,7292875,7292876,7292877,7292878,7292879,7292880,7292881,7292882,7292883,7292884,7292885,7292886,7292887,7292888,7292889,7292890,7292891,7292892,7292893,7292894,7292895,7292896,7292897,7292898,7292899,7292900,7292901,7292902,7292903,7292904,7292905,7292906,7292907,7292908,7292909,7292910,7292911,7292912,7292913,7292914,7292915,7292916,7292917,7292918,7292919,7292920,7292921,7292922,7292923,7292924,7292925,7292926,7292927,7292928,7292929,7292930,7292931,7292932,7292933,7292934,7292935,7292936,7292937,7292938,7292939,7292940,7292941,7292942,7292943,7292944,7292945,7292946,7292947,7292948,7292949,7292950,7292951,7292952,7292953,7292954,7292955,7292956,7292957,7292958,7292959,7292960,7292961,7292962,7292963,7292964,7292965,7292966,7292967,7292968,7292969,7292971,7292972,7292973,7292974,7292975,7292976,7292977,7292978,7292979,7292980,7292981,7292982,7292983,7292984,7292985,7292986,7292987,7292988,7292989,7292990,7292991,7292992,7292993,7292994,7292995,7292996,7292997,7292998]

    for i in list1:
        # todo
        url = "https://www.dingdiann.com/ddk13534/%d.html" % i

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

        html = str(html_bytes, encoding="utf-8", errors="ignore")


        myparser = MyParser()
        myparser.feed(html)

        logging.info("----------------------- parse fini -----------------------------")

    logging.info("=================================== end =====================================")