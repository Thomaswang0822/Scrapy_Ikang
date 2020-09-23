# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"

class IkangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product = scrapy.Field()
    price = scrapy.Field()
    sales = scrapy.Field()
    exams = scrapy.Field()

