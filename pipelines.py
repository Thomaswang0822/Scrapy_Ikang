# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class IkangPipeline:
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = '000822'
        database = 'MedicalDB'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        command = """INSERT INTO "ikang"("Product","Price","Sales","Exams") VALUES(%s,%s,%s,%s)"""
        param = (
            item["product"],
            item["price"],
            item["sales"],
            item["exams"],
                 )
        self.cur.execute(command, param)
        self.connection.commit()
        # return item
