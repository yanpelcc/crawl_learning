import sqlalchemy
import json
import pandas as pd

with open('pyjobs.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data, columns=['job', 'area', 'edu', 'exp', 'salary'])
print(df)

mysqlInfo = {
    "host": '127.0.0.1',
    "user": 'root',
    "password": 'yanpelc137',
    "database": 'crawler',
    "port": 3306,
    "charset": 'utf8'
}

engine = sqlalchemy.create_engine(
    'mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % mysqlInfo)

df.to_sql('pyjobs', engine, 'crawler', if_exists='replace', index=True)
