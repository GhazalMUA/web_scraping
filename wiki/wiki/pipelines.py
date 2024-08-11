# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
from scrapy.exceptions import DropItem

class WikiPipeline:
    
    def __init__(self):
        self.con= sqlite3.connect('countries.db')
        self.cur = self.con.cursor()
        self.create_table()
        
    def create_table(self):
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS country(
            name TEXT PRIMARY KEY, capital TEXT, population INTEGER 
        )""")
        
    def process_item(self, item, spider):
        self.cur.execute(""" 
            INSERT OR IGNORE INTO country VALUES (?,?,?)
        """,
            (item['name'] , item['capital'] , item['population'])
        )
        self.con.commit()
        return item
       

'''
    yeki dg az karbord hai ke in pipeline ha daran ine ke mitonim
    etelaat ro filter konim masalan begim faghat on keshvarai save
    beshan ke jaamiyateshon balata az 50 milion nafar bashe. faghat
    inke chandta nokte ro bayad raayat konim:
    1- bayad begim ag bishtar az 50m nabod nemikhyamesh yani drop esh kon k bayad import she
    2- tooye settings tooye bakhshe pipeline bayadf moarefi beshe va behesh ye adad bedim
    harchi adad kochiktar bashe taghadome bishtari ham dare. 
'''

    
class PopulationPipeline:
    
    def process_item(self, item, spider):
        if int(item['population']) < 50000000:
            raise DropItem('oops this population is less than 50M ... ')
        return item     
