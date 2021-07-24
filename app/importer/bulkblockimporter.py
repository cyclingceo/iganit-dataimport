import csv


class BulkBlockImporter:
    def net_orders(self):
        net_orders_sql = 'select t1.trading_date,t1.isin,t1.client_name,t1.trade_type,t1.quantity_traded,t1.deal_type ' \
                         'from bulk_block_deals t1 EXCEPT select t1.trading_date,t1.isin,t1.client_name,t1.trade_type,t1.quantity_traded' \
                         ',t1.deal_type from bulk_block_deals t1 INNER JOIN bulk_block_deals t2 ' \
                         'ON t1.trading_date = t2.trading_date AND t1.isin = t2.isin AND t1.client_name = t2.client_name AND ' \
                         't1.deal_type = t2.deal_type AND t1.quantity_traded = t2.quantity_traded AND t1.trade_type <> t2.trade_type'
