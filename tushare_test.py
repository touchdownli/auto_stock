# -*- coding:utf-8 -*-
import tushare as ts
import pandas as pd
from datetime import datetime

def profit_ratio_ordered():
 df = ts.profit_data(top=30)
 close_df = ts.get_today_all()
 join_df = df.set_index('code').join(close_df.set_index('code'),how='inner',lsuffix='left')
 select_df = join_df[['name','trade','divi','year','shares','report_date']]
 select_df['divi_trade'] = select_df.divi/select_df.trade/10*(10+select_df.shares)/10
 select_df = select_df.sort_values('divi_trade',ascending=False)
 select_df.to_csv('ts_test.result')
 print("write file done")

def do_trans(df, engine):
  df.to_sql('mock_trans', engine, if_exists='append', index=False)

def select_share():
  df = pd.read_csv("today_all.csv")
  #df = ts.get_today_all()
  # 获取股价上涨超过9%的股票
  selected_codes = df[df['changepercent'] > 10][['code','name','trade','changepercent']].sort_values('changepercent', ascending=False)
  # 遍历每支股票,下买单
  items = {}
  length = len(selected_codes.index)
  date = datetime.now().strftime('%Y-%m-%d')
  for item in selected_codes.iterrows():
    # print(item[1]['code'],item[1]['name'])
    items.setdefault('code',[])
    items.setdefault('name',[])
    items.setdefault('trans_type',['buy' for i in range(length)])
    items.setdefault('price',[])
    items.setdefault('count',[100 for i in range(length)])
    items.setdefault('trans_date',[date for i in range(length)])
    
    items['code'].append(item[1]['code'])
    items['name'].append(item[1]['name'])
    items['price'].append(item[1]['trade'])

  return items
    
  '''
  ts.set_broker('zxjt', user='', passwd='')
  ts.get_broker()
  api = ts.TraderAPI('zxjt')
  api.login()
  baseinfo = api.baseinfo()
  api.buy('code',price=10.1,count=1000)
  api.entrust_list()
  api.cancel(orderno='23232,2323',orderdate='20180115,20180116')
  api.deal_list(begin=20180115,end=20180116)
  '''

from sqlalchemy import create_engine
if __name__ == '__main__':
  engine = create_engine('mysql+pymysql://root@127.0.0.1/auto_stock?charset=utf8')
  items = select_share()
  if items:
    df = pd.DataFrame.from_dict(items)
    do_trans(df,engine)
