from yoyo import step

steps = [
     step("CREATE TABLE BULK_BLOCK_DEALS(" \
          "ISIN VARCHAR(20) ," \
          "TRADING_DATE DATE," \
          "CLIENT_NAME VARCHAR(512) ," \
          "TRADE_TYPE VARCHAR(8) ," \
          "QUANTITY_TRADED DECIMAL(30,2) ," \
          "TRADE_PRICE DECIMAL(14,2) ," \
          "EXCHANGE VARCHAR(8) ," \
          "DEAL_TYPE VARCHAR(8) ," \
          "CONSTRAINT PK_BULK_BLOCK_DEALS PRIMARY KEY(ISIN, TRADING_DATE,EXCHANGE,DEAL_TYPE,CLIENT_NAME,TRADE_TYPE))"
          )
]