# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class IkangPipeline:
    ## modify here
    def open_spider(self, spider):
        hostname = 'YOUR HOSTNAME'      #if you has a local DB, it's 'localhost'
        username = 'YOUR USERNAME'   # Usually (default) postgres 
        password = 'YOUR PASSWORD'
        database = 'YOUR DATABASE NAME'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        command = """INSERT INTO "ikang_ook"("Product","Price","Sales","Exam","Content","Url") VALUES(%s,%s,%s,%s,%s,%s)"""
        param = (
            item["product"],
            item["price"],
            item["sales"],
            item["exams"],
            item['content'],
            item['url']
                 )
        self.cur.execute(command, param)
        self.connection.commit()
        # return item
