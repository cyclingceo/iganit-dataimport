import csv
import json
from zipfile import ZipFile
from io import BytesIO

import requests

from app.dbaccess import dbconnection


class BhavCopyImporter:
    def fetch(self,exchange) :
        if("NSE" == exchange):
            NSEBhavCopyImporter().fetch()
        elif("BSE" == exchange):
            BSEBhavCopyImporter().fetch()


class NSEBhavCopyImporter:
    def fetch(self):
        insert_sql = 'INSERT INTO public.DAILY_BHAV_COPY(isin,trading_date, nse_open, nse_high, nse_low,' \
                     'nse_close, nse_last, nse_prev_close,nse_trades,nse_shares_traded,nse_turnover)' \
                     ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (isin,trading_date) DO ' \
                     'UPDATE SET nse_open=%s,nse_high=%s, nse_low=%s, nse_close=%s,' \
                     'nse_last=%s, nse_prev_close=%s, nse_trades=%s, nse_shares_traded=%s,nse_turnover=%s' \
                     ' WHERE public.DAILY_BHAV_COPY.isin = %s and DAILY_BHAV_COPY.trading_date = %s'
        conn = dbconnection.DBConnection().getDBConnection()
        cur = conn.cursor()
        download_path='/home/jayramj/tmp/bhavcopy/'
        print('Importing NSE BhavCopy')
        headers = {'Host': 'www1.nseindia.com',
                   'Accept':'*/*',
                   'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
                   'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'en-US,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Origin': 'https://www1.nseindia.com', 'Connection': 'keep-alive',
                   'Referer': 'https://www1.nseindia.com/products/content/equities/equities/archieve_eq.htm',
                   'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site':'same-origin', 'Sec-Fetch-User': '?1'}
        file_path = 'https://www1.nseindia.com/content/historical/EQUITIES/2021/JUL/cm16JUL2021bhav.csv.zip'
        response = requests.get(file_path,headers=headers,stream=True)
        zipfile = ZipFile(BytesIO(response.content))
        csv_file_name = zipfile.namelist().pop()
        zipfile.extractall(download_path)
        csv_file_name = download_path + csv_file_name
        with open(csv_file_name, newline='') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        field_names = csv_data.pop(0)
        field_names = [x.lstrip(' ') for x in field_names]
        print(field_names)
        for record in csv_data:
            sd = dict(zip(field_names, record))
            cur.execute(insert_sql,[sd.get('ISIN'),sd.get('TIMESTAMP'),sd.get('OPEN'),sd.get('HIGH'),sd.get('LOW'),
                                    sd.get('CLOSE'),sd.get('LAST'),sd.get('PREVCLOSE'),sd.get('TOTTRDQTY'),sd.get('TOTALTRADES'),sd.get('TOTTRDVAL')
                                    ,sd.get('OPEN'),sd.get('HIGH'),sd.get('LOW'),
                                    sd.get('CLOSE'),sd.get('LAST'),sd.get('PREVCLOSE'),sd.get('TOTTRDQTY'),sd.get('TOTALTRADES'),sd.get('TOTTRDVAL')
                                    ,sd.get('ISIN'),sd.get('TIMESTAMP')])
            print(sd)
        conn.commit()
        cur.close()
        conn.close()

class BSEBhavCopyImporter:
    def fetch(self):
        insert_sql = 'INSERT INTO public.DAILY_BHAV_COPY(isin,trading_date, bse_open, bse_high, bse_low,' \
                     'bse_close, bse_last, bse_prev_close,bse_trades,bse_shares_traded,bse_turnover)' \
                     ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (isin,trading_date) DO ' \
                     'UPDATE SET bse_open=%s,bse_high=%s, bse_low=%s, bse_close=%s,' \
                     'bse_last=%s, bse_prev_close=%s, bse_trades=%s, bse_shares_traded=%s,bse_turnover=%s' \
                     ' WHERE public.DAILY_BHAV_COPY.isin = %s and DAILY_BHAV_COPY.trading_date = %s'
        conn = dbconnection.DBConnection().getDBConnection()
        cur = conn.cursor()
        download_path='/home/jayramj/tmp/bhavcopy/'
        print('Importing BSE BhavCopy')
        headers = {'Host': 'www.bseindia.com',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Origin': 'https://www.bseindia.com', 'Connection': 'keep-alive',
                   'Referer': 'https://www.bseindia.com/markets/marketinfo/BhavCopy.aspx'}
        file_path = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ_ISINCODE_160721.zip'
        response = requests.get(file_path,headers=headers,stream=True)
        zipfile = ZipFile(BytesIO(response.content))
        csv_file_name = zipfile.namelist().pop()
        print(csv_file_name)
        zipfile.extractall(download_path)
        csv_file_name = download_path + csv_file_name
        with open(csv_file_name, newline='') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        field_names = csv_data.pop(0)
        field_names = [x.lstrip(' ') for x in field_names]
        print(field_names)
        for record in csv_data:
            sd = dict(zip(field_names, record))
            cur.execute(insert_sql, [sd.get('ISIN_CODE'), sd.get('TRADING_DATE'), sd.get('OPEN'), sd.get('HIGH'), sd.get('LOW'),
                                     sd.get('CLOSE'), sd.get('LAST'), sd.get('PREVCLOSE'), sd.get('NO_TRADES'),
                                     sd.get('NO_OF_SHRS'), sd.get('NET_TURNOV')
                , sd.get('OPEN'), sd.get('HIGH'), sd.get('LOW'),
                                     sd.get('CLOSE'), sd.get('LAST'), sd.get('PREVCLOSE'), sd.get('NO_TRADES'),
                                     sd.get('NO_OF_SHRS'), sd.get('NET_TURNOV')
                , sd.get('ISIN_CODE'), sd.get('TRADING_DATE')])
            print(sd)
        conn.commit()
        cur.close()
        conn.close()