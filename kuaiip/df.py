import pandas
import json
import sqlalchemy

with open('ip.json', 'r') as f:
    data = json.load(f)

df = pandas.DataFrame(columns=['ip', 'port', 'ty', 'location', 'speed'])

for i in range(len(data)):
    ndf = pandas.DataFrame(data[i])
    df = df.append(ndf, ignore_index=True)

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

df.to_sql('ip', engine, 'crawler', 'replace', index=True)
