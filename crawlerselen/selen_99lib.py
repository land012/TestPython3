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
from selen_demo import a_id


logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


def parse_html(p_id, p_chapter, p_file, p_browser):
    logging.info("------------------------- request {} begin -------------------------".format(p_chapter))

    url = "https://www.99csw.com/book/{}/{}.htm".format(p_id, p_chapter)
    p_browser.get(url)
    logging.info("------------------------- request {} end -------------------------".format(p_chapter))

    height = p_browser.execute_script("return action=document.body.scrollHeight")
    logging.info(height)

    while True:
        p_browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(0.2)
        height2 = p_browser.execute_script("return action=document.body.scrollHeight")
        logging.info(height2)
        if height2 == height:
            break

        height = height2

    # logging.info(len(ff.find_element_by_id("content").find_elements_by_tag_name("div")))

    p_file.write("\n\n\n")
    # h1
    p_file.write(p_browser.find_elements_by_xpath("//div[@id='content']/h2")[0].text)
    p_file.write("\n")
    # h2
    p_file.write(p_browser.find_elements_by_xpath("//div[@id='content']/h2[@class='h2']")[0].text)
    p_file.write("\n")

    for div in p_browser.find_elements_by_xpath("//div[@id='content']/div"):
        if div.value_of_css_property("display") == "block":
            p_file.write(div.text)
            p_file.write("\n")


def main():
    logging.info("------------------------- main begin -------------------------")
    ff_options = Options()
    ff_options.add_argument("--headless")

    ff = Firefox(executable_path=r"D:\ProgramGreen\Mozilla Firefox\geckodriver.exe", firefox_options=ff_options)
    ff.set_page_load_timeout(20)


    # todo modify
    list1 = [208471,208472,208473,208474,208475,208476,208477,208478,208479,208480,208481,208482,208483]

    # ff.get("https://www.99lib.net/book/9031/index.htm")  # 第一次请求似乎有些问题

    try:
        f = open("1.log", mode='w', encoding='utf-8')

        for chapter in list1:
            count = 0
            while count < 3:
                try:
                    parse_html(a_id, chapter, f, ff)
                    break
                except TimeoutException as e2:
                    logging.info("------------------ {} timeout -------------------".format(chapter))
                    count += 1

            if count >= 3:
                logging.error("---------------------- {} req failed ----------------------".format(chapter))
                return

        f.close()

    except Exception as e:
        logging.exception(e)

    logging.info("------------------------------------- end -------------------------------------")

    # html = ff.page_source
    #
    # f = open("demo.log", mode='w', encoding='utf-8')
    # f.write(html)
    # f.close()

    ff.close()

if __name__ == "__main__":
    main()
