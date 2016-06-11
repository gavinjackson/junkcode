import scrapy
import time
from openpyxl import Workbook
import sqlite3

# This app prints data to standard out, creates a spreadsheet and updates an sqlite3 database

class EcocrackenbackSpider(scrapy.Spider):
    name = 'Ecocrackenback Availability'
    wb = Workbook()
    properties = {
        '33': 'Ecocrackenback 2',
        '34': 'Ecocrackenback 3',
        '35': 'Ecocrackenback 4',
        '36': 'Ecocrackenback 5',
        '37': 'Ecocrackenback 7',
        '38': 'Ecocrackenback 9',
        '39': 'Ecocrackenback 10',
        '40': 'Ecocrackenback 11',
        '41': 'Ecocrackenback 12',
        '42': 'Ecocrackenback 13',
        '43': 'Ecocrackenback 14',
        '46': 'Ecocrackenback 15',
        '44': 'Ecocrackenback 16',
        '50': 'Ecocrackenback 17',
        '45': 'Ecocrackenback 18',
        '49': 'Ecocrackenback 19'
    }
    ws1 = wb.active
    ws1.append(["Ecocrackenback bookings last extracted {0}".format(time.strftime("%c"))])
    
    start_urls = [ 'http://www.jindabyneaccommodationcentre.com.au/accommodation/{0}'.format(p) for p in properties.keys() ]

    conn = sqlite3.connect('./eco.db')
    c = conn.cursor()
    c.execute("insert into eco_execution_run values (NULL, '{0}');".format(time.strftime("%Y-%m-%d %H:%M:%S")))
    eid = c.lastrowid
    conn.commit()

    def parse(self, response):
        print('\n= {0} ='.format(self.properties[response.url.split('/')[-1:][0]]))
        self.c.execute("insert into eco_property values (NULL, {0}, '{1}', '{2}');".format(self.eid, self.properties[response.url.split('/')[-1:][0]], response.url.split('/')[-1:][0]))
        pid = self.c.lastrowid
        self.conn.commit()
        ws = self.wb.create_sheet(title="{0}".format(self.properties[response.url.split('/')[-1:][0]]))
        print('*'*80)
        attributes = {}
        rows = response.xpath('//*[@id="ipage"]/div[4]/table/tr')
        for index, row in enumerate(rows):
            if index > 0:
                print('== {0} =='.format(row.xpath('td[1]/text()').extract()[0]))
                self.c.execute("insert into eco_month values (NULL, {0}, {1}, '{2}');".format(self.eid, pid, row.xpath('td[1]/text()').extract()[0]))
                mid = self.c.lastrowid
                self.conn.commit()
                ws.append([row.xpath('td[1]/text()').extract()[0]])
                print('AVAILABLE {0}'.format(row.css('.available').xpath('@title').extract()))
                for str_date in row.css('.available').xpath('@title').extract():
                    from datetime import datetime
                    date_object = datetime.strptime(str_date, '%a %d-%b-%Y')
                    self.c.execute("insert into eco_day values (NULL, {0}, 'AVAILABLE', '{1}', '{2}')".format(mid, str_date.split(' ')[0], date_object.strftime('%Y-%m-%d')))
                    self.conn.commit()
                ws.append(['AVAILABLE'] + row.css('.available').xpath('@title').extract())
                print('BOOKED {0}'.format(row.css('.booked').xpath('@title').extract()))
                for str_date in row.css('.booked').xpath('@title').extract():
                    from datetime import datetime
                    date_object = datetime.strptime(str_date, '%a %d-%b-%Y')
                    self.c.execute("insert into eco_day values (NULL, {0}, 'BOOKED', '{1}', '{2}')".format(mid, str_date.split(' ')[0], date_object.strftime('%Y-%m-%d')))
                    self.conn.commit()
                ws.append(['BOOKED'] + row.css('.booked').xpath('@title').extract())
        ws.append([''])
    def closed(self, reason):
        self.wb.save(filename = "./output.xlsx")
        self.conn.commit()
        self.c.close()
