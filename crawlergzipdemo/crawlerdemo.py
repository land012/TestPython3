# coding: utf-8
"""
# Created by xudazhou at 2019/8/17

"""
import logging
import urllib.request
import urllib.error
from html.parser import HTMLParser
import socket
import ssl
import gzip


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    ssl._create_default_https_context = ssl._create_unverified_context

    # url = "https://www.qisuu.la/du/30/30992/9534396.html"
    url = "https://wap.qisuu.34395.html"

    try:
        # urllib.error.HTTPError: HTTP Error 502: Bad Gateway
        # urllib.error.URLError: <urlopen error _ssl.c:761: The handshake operation timed out>
        resp = urllib.request.urlopen(url, timeout=20)
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

    logging.info("res type {}, len={}".format(type(res), len(res)))  # res type <class 'bytes'>
    logging.info("{} {}".format(hex(res[0]), hex(res[1])))

    html = str(gzip.decompress(res), encoding="utf-8", errors="ignore")

    f = open("demo.log", mode='w', encoding='utf-8')
    f.write(html)
    f.close()

    # 每章下载到不同文件
    # myparser = MyParser(1)
    # myparser.feed(html)




