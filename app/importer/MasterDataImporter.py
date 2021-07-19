import csv
import json

import requests

from app.dbaccess import dbconnection


class BSEMasterDataImporter:

    def fetch(self):
        params = {'Group': '', 'Scripcode': '', 'industry': '', 'segment': 'Equity', 'status': 'Active'}
        headers = {'Host': 'api.bseindia.com',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
                   'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'en-US,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Origin': 'https://www.bseindia.com', 'Connection': 'keep-alive',
                   'Referer': 'https://www.bseindia.com/', 'TE': 'Trailers'}
        response = requests.get('https://api.bseindia.com/BseIndiaAPI/api/ListofScripData/w',
                                headers=headers, params=params, )

        stock_list = json.loads(response.content.decode('latin-1'))
        conn = dbconnection.DBConnection().getDBConnection()
        cur = conn.cursor()

        for sd in stock_list:
            print(sd)
            insert_sql = 'INSERT INTO public.master_stock_list(isin, bse_security_code, bse_issuer_name, bse_security_id,' \
                         'bse_security_name, bse_group, bse_face_value,bse_industry, bse_segment, bse_nsurl, listed_on_bse)' \
                         ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (isin) DO ' \
                         'UPDATE SET bse_security_code=%s,bse_issuer_name=%s, bse_security_id=%s, bse_security_name=%s,' \
                         'bse_group=%s, bse_face_value=%s, bse_industry=%s, bse_segment=%s, bse_nsurl=%s, listed_on_bse=%s' \
                         ' WHERE public.master_stock_list.isin = %s'

            cur.execute(insert_sql,
                        [sd.get('ISIN_NUMBER'), sd.get('SCRIP_CD'), sd.get('Issuer_Name'), sd.get('scrip_id'),
                         sd.get('Scrip_Name'), sd.get('GROUP'), sd.get('FACE_VALUE'),
                         sd.get('INDUSTRY'), sd.get('Segment'), sd.get('NSURL'), 'TRUE', sd.get('SCRIP_CD'),
                         sd.get('Issuer_Name'), sd.get('scrip_id'), sd.get('Scrip_Name'), sd.get('GROUP'),
                         sd.get('FACE_VALUE'),
                         sd.get('INDUSTRY'), sd.get('Segment'), sd.get('NSURL'), 'TRUE', sd.get('ISIN_NUMBER')])
        conn.commit()
        cur.close()
        conn.close()


class NSEMasterDataImporter:
    def fetch(self):
        insert_sql = 'INSERT INTO public.master_stock_list(isin,nse_symbol, nse_name_of_company, nse_series, nse_date_of_listing,' \
                     'nse_paid_up_value, nse_market_lot, nse_face_value,listed_on_nse)' \
                     ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (isin) DO ' \
                     'UPDATE SET nse_symbol=%s,nse_name_of_company=%s, nse_series=%s, nse_date_of_listing=%s,' \
                     'nse_paid_up_value=%s, nse_market_lot=%s, nse_face_value=%s, listed_on_nse=%s' \
                     ' WHERE public.master_stock_list.isin = %s'

        conn = dbconnection.DBConnection().getDBConnection()
        cur = conn.cursor()

        response = requests.get('https://www1.nseindia.com/content/equities/EQUITY_L.csv')
        csv_data = list(csv.reader(response.text.strip().split('\n')))
        field_names = csv_data.pop(0)
        field_names = [x.lstrip(' ') for x in field_names]
        print(field_names)
        for record in csv_data:
            sd = dict(zip(field_names, record))
            print(sd.get('ISIN NUMBER'))
            cur.execute(insert_sql,
                        [sd.get('ISIN NUMBER'), sd.get('SYMBOL'), sd.get('NAME OF COMPANY'), sd.get('SERIES'),
                         sd.get('DATE OF LISTING'), sd.get('PAID UP VALUE'), sd.get('MARKET LOT'),
                         sd.get(' FACE VALUE'), 'TRUE',
                         sd.get('SYMBOL'), sd.get('NAME OF COMPANY'), sd.get('SERIES'), sd.get(' DATE OF LISTING'),
                         sd.get('PAID UP VALUE'),
                         sd.get(' MARKET LOT'), sd.get(' FACE VALUE'), 'TRUE', sd.get('ISIN NUMBER')])
        conn.commit()
        cur.close()
        conn.close()
