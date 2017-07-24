# -*- coding: utf-8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse
import time

from PhantomJS_Crawler.settings import PATH_PhantomJS,SearchKeyWords
from selenium.webdriver.common.keys import Keys

global driver
driver = webdriver.PhantomJS(PATH_PhantomJS)
print("Phantomjs is starting..............")

js= """
    function scrollToBottom() {
        var Height = document.body.clientHeight,  //文本高度
            screenHeight = window.innerHeight,  //屏幕高度
            INTERVAL = 100,  // 滚动动作之间的间隔时间
            delta = 500,  //每次滚动距离
            curScrollTop = 0;    //当前window.scrollTop 值

        var scroll = function () {
            curScrollTop = document.body.scrollTop;
            window.scrollTo(0,curScrollTop + delta);
        };

        var timer = setInterval(function () {
            var curHeight = curScrollTop + screenHeight;
            if (curHeight >= Height){   //滚动到页面底部时，结束滚动
                clearInterval(timer);
            }
            scroll();
        }, INTERVAL)
    }
    scrollToBottom()
    """




class JSMiddleware(object):
    @classmethod
    def process_request(cls, request, spider):

        if request.meta.has_key('PhantomJs'):
            driver.get(request.url)

            driver.execute_script(js)
            time.sleep(5)

            '''
            driver.find_element_by_id("KeyWord_kw2").send_keys(SearchKeyWords)
            time.sleep(1)
            driver.find_element_by_id("JobLocation").send_keys(u'上海')
            time.sleep(1)
            driver.find_element_by_id("JobLocation").send_keys(Keys.ENTER)
            time.sleep(0.5)
            print("input is over==============================")
            '''
            content = driver.page_source.encode('utf-8')
            driver.quit()
            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)


