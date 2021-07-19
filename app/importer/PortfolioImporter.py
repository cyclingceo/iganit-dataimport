import csv
import json

from app.dbaccess import dbconnection


class IDirectImporter:
    def fetch(self):
        insert_sql = 'INSERT INTO IDIRECT_PORTFOLIO(title,user_id,entries) ' \
                     'VALUES(%s,%s,%s)'
        print("Importing IDirect Portfolio")
        portfolio_csv = '/home/jayramj/Self/investing/090721_PortFolioEqtSummary.csv'
        portfolio_json = []
        conn = dbconnection.DBConnection().getDBConnection()
        cur = conn.cursor()
        with open(portfolio_csv, newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_data = list(csv_reader)
            csv_data.pop(0)
            field_names = ['Stock Symbol', 'Company Name', 'ISIN Code', 'Qty']
            field_names = [x.lstrip(' ') for x in field_names]
            for record in csv_data:
                sd = dict(zip(field_names, record))
                portfolio_json.append(sd)
        print(json.dumps(portfolio_json, indent=4))
        cur.execute(insert_sql,
                    ['default', 1, json.dumps(portfolio_json, indent=4)])
        conn.commit()
        cur.close()
        conn.close()
