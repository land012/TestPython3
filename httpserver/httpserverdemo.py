# coding: utf-8
"""
# Created by xudazhou at 2019/8/17
"""

import http.server
import urllib
import sys
import logging
import traceback


class Request(http.server.CGIHTTPRequestHandler):

    def do_GET(self):
        try:
            querypath = urllib.parse.urlparse(self.path)
            logging.info(querypath.path)
            logging.info(querypath.query)

            if querypath.path == "/pic":
                self.send_response(200)
                self.send_header("Content-Type", "image/jpg")
                self.end_headers()

                f = open("StokePero.jpg", mode="b")
                self.wfile.write(f.read())
                f.close()
            else:
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write("hello http server".encode())
        except:
            logging.exception(sys.exc_info())
            # logging.error(traceback.format_exc())

    def do_POST(self):
        self.do_GET()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    server = http.server.HTTPServer(('', 8888), Request)
    print("Start Server ...")
    server.serve_forever()