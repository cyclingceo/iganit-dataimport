from yoyo import step

steps = [
  step("CREATE TABLE IDIRECT_PORTFOLIO(" \
       "ID SERIAL PRIMARY KEY," \
       "TITLE VARCHAR(256)," \
       "USER_ID INTEGER NOT NULL," \
       "ENTRIES json )"
       )
]