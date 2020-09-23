import scrapy
from ikang.items import IkangItem
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains


class IkangspiderSpider(scrapy.Spider):
    name = 'ikangSpider'
    allowed_domains = ['mall.ikang.com']
    start_urls = ['http://mall.ikang.com/searchList?product_first_type_id=232']
    handle_httpstatus_list = [301]

    ''' Wrap up a function
    Workflow:
    click the proudct element (good) in our loop
    swtich to the new tab
    find all the elements by xpath
    extract all the texts and concatenate them into a string
    close the tab
    switch back to the primary tab 
    return the string
    '''
    def getDetail(self, driver, good):
        ActionChains(driver).move_to_element(good).click().perform()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)  # pause for driver to load the page
        exam_list = driver.find_elements_by_xpath('//table/tbody/tr/td/tr/td[1]')
        exam_str = ''
        for exam in exam_list:
            exam_str = exam_str + exam.text + ' '
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return exam_str

    def parse(self, response):
        # Set Options
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')
        # Don't load images, improve speed
        chrome_options.add_argument('blink-settings=imagesEnabled=false')

        # initialize driver
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.implicitly_wait(1) # pause to cheat anti-scrawl mech
        url = 'http://mall.ikang.com/searchList?product_first_type_id=232'
        driver.get(url)
        driver.maximize_window()    # to see all elements

        js = "var q=document.documentElement.scrollTop=800"
        # use sleep()， implicitly wait doesn't work
        time.sleep(1) #
        driver.execute_script(js)
        time.sleep(1) #

        # handle first page
        goods_list = driver.find_elements_by_xpath('//div[@class="goods-card-right"]')
        for i in range( len(goods_list) ):
            ikang_item = IkangItem()
            good = goods_list[i]
            ikang_item['product'] = good.find_element_by_xpath('./p').text
            ikang_item['price'] = good.find_element_by_xpath('./div[1]/div[1]').text
            ikang_item['sales'] = good.find_element_by_xpath('./div[1]/div[2]').text
            ### use the helper function
            ikang_item['exams'] = self.getDetail(driver=driver, good=good)
            yield ikang_item


        # looping, click button 5 times, get data in page 2-6
        for i in range(5):
            driver.implicitly_wait(1)
            driver.find_element_by_xpath('//button[@class="btn-next"]').click()
            self.logger.info("Going to the {} page".format(i+2))

            driver.implicitly_wait(1)
            goods_list = driver.find_elements_by_xpath('//div[@class="goods-card-right"]')
            for good in goods_list:
                ikang_item = IkangItem()
                ikang_item['product'] = good.find_element_by_xpath('./p').text
                ikang_item['price'] = good.find_element_by_xpath('./div[1]/div[1]').text
                ikang_item['sales'] = good.find_element_by_xpath('./div[1]/div[2]').text
                ### use the helper function
                ikang_item['exams'] = self.getDetail(driver=driver, good=good)
                yield ikang_item

