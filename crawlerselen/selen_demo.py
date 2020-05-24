# coding: utf-8
"""
# Created by xudazhou at 2020/1/5

页面滚动加载，且用了 js 打乱页面段落顺序
"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import logging


logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


a_id = 9033

if __name__ == "__main__":
    logging.info("------------------------- main begin -------------------------")

    ff_options = Options()
    ff_options.add_argument("--headless")

    ff = Firefox(executable_path=r"D:\ProgramGreen\Mozilla Firefox\geckodriver.exe", firefox_options=ff_options)
    ff.set_page_load_timeout(10)

    logging.info("------------------------- request begin -------------------------")

    url = "https://www.99csw.com/book/{}/index.htm".format(a_id)

    count = 0
    while count < 3:
        try:
            count += 1
            ff.get(url)
            break
        except TimeoutException as e:
            logging.error("------------------------- request timeout -------------------------")
            if count >= 3:
                logging.error("------------------------- request retry 3 times failed -------------------------")
                exit(1)

    logging.info("------------------------- request end -------------------------")

    # time.sleep(5)

    height = ff.execute_script("return action=document.body.scrollHeight")
    logging.info(height)

    while True:
        ff.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(0.2)
        height2 = ff.execute_script("return action=document.body.scrollHeight")
        logging.info(height2)
        if height2 == height:
            break

        height = height2

    a_list = ff.find_elements_by_xpath("//div[@id='right']/dl//a")

    f = open("demo.log", mode='w', encoding='utf-8')

    for a in a_list:
        href = a.get_attribute("href")
        href_arr = href.rsplit("/", maxsplit=1)
        f.write(href_arr[1][:href_arr[1].find(".")])
        f.write(",")

    ff.close()

    logging.info("------------------------- main end -------------------------")

