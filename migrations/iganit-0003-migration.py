from yoyo import step

steps = [
  step("CREATE TABLE DAILY_BHAV_COPY(" \
       "ISIN VARCHAR(20) ," \
       "TRADING_DATE DATE," \
       "BSE_OPEN DECIMAL(14,2)," \
       "BSE_HIGH DECIMAL(14,2)," \
       "BSE_LOW DECIMAL(14,2)," \
       "BSE_CLOSE DECIMAL(14,2)," \
       "BSE_LAST DECIMAL(14,2)," \
       "BSE_PREV_CLOSE DECIMAL(14,2)," \
       "BSE_TRADES BIGINT," \
       "BSE_SHARES_TRADED BIGINT," \
       "BSE_TURNOVER DECIMAL(30,2)," \
       "NSE_OPEN DECIMAL(14,2)," \
       "NSE_HIGH DECIMAL(14,2)," \
       "NSE_LOW DECIMAL(14,2)," \
       "NSE_CLOSE DECIMAL(14,2)," \
       "NSE_LAST DECIMAL(14,2)," \
       "NSE_PREV_CLOSE DECIMAL(14,2)," \
       "NSE_TRADES BIGINT," \
       "NSE_SHARES_TRADED BIGINT," \
       "NSE_TURNOVER DECIMAL(30,2), " \
       "CONSTRAINT PK_DAILY_BHAV_COPY PRIMARY KEY(ISIN, TRADING_DATE))"
       )
]