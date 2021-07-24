import csv
from datetime import datetime
from json import dumps

import requests

from app.dbaccess import dbconnection
from app.importer.bulkblockimporter import BulkBlockImporter


class BulkImporter(BulkBlockImporter):
    def fetch(self):
        file_path = '/home/jayramj/projects/iganit/masterdata-mgmt/downloads/bulkblock/BSE_Bulk.csv'
        field_names = ['trading_date', 'symbol', 'security_name', 'client_name','trade_type', 'quantity_traded', 'trade_price',
                       'exchange', 'deal_type']
        insert_sql = 'INSERT INTO public.bulk_block_deals (isin, trading_date, client_name, trade_type, quantity_traded,' \
                       ' trade_price, exchange, deal_type) SELECT isin , %s, %s, %s, %s, %s, %s, %s ' \
                       'from master_stock_list where bse_security_code = %s'
        conn = dbconnection.DBConnection().getDBConnection()
        cur = conn.cursor()
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
            print(len(csv_data))
        print(field_names)
        csv_data.pop(0)
        counter = 0
        for record in csv_data:
            if(len(record) != 7) :
                print(record)
                continue
            record.append('BSE')
            record.append('Bulk')
            sd = dict(zip(field_names, record))
            cur.execute(insert_sql,[datetime.strptime(sd.get('trading_date'),'%d/%m/%Y').strftime('%d-%b-%Y'), sd.get('client_name'), sd.get('trade_type'),
                                   sd.get('quantity_traded').replace(',',''), sd.get('trade_price').replace(',',''),
                                   sd.get('exchange'), sd.get('deal_type'), sd.get('symbol')])
            counter = counter + 1
            #print(counter,sd.get('symbol'))
        conn.commit()
        cur.close()
        conn.close()



class BlockImporter(BulkBlockImporter):
    def fetch(self):
        file_path = '/home/jayramj/projects/iganit/masterdata-mgmt/downloads/bulkblock/BSE_Block.csv'
        field_names = ['trading_date', 'symbol', 'security_name', 'client_name','trade_type', 'quantity_traded', 'trade_price',
                       'exchange', 'deal_type']
        insert_sql = 'INSERT INTO public.bulk_block_deals (isin, trading_date, client_name, trade_type, quantity_traded,' \
                       ' trade_price, exchange, deal_type) SELECT isin , %s, %s, %s, %s, %s, %s, %s ' \
                       'from master_stock_list where bse_security_code = %s'
        conn = dbconnection.DBConnection().getDBConnection()
        cur = conn.cursor()
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
            print(len(csv_data))
        print(field_names)
        csv_data.pop(0)
        counter = 0
        for record in csv_data:
            if(len(record) != 7) :
                print(record)
                continue
            record.append('BSE')
            record.append('Block')
            sd = dict(zip(field_names, record))
            cur.execute(insert_sql,[datetime.strptime(sd.get('trading_date'),'%d/%m/%Y').strftime('%d-%b-%Y'), sd.get('client_name'), sd.get('trade_type'),
                                   sd.get('quantity_traded').replace(',',''), sd.get('trade_price').replace(',',''),
                                   sd.get('exchange'), sd.get('deal_type'), sd.get('symbol')])
            counter = counter + 1
            #print(counter,sd.get('symbol'))
        conn.commit()
        cur.close()
        conn.close()
