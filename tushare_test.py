# -*- coding:utf-8 -*-
import tushare as ts
import pandas as pd

def profit_ratio_ordered():
 df = ts.profit_data(top=30)
 close_df = ts.get_today_all()
 join_df = df.set_index('code').join(close_df.set_index('code'),how='inner',lsuffix='left')
 select_df = join_df[['name','trade','divi','year','shares','report_date']]
 select_df['divi_trade'] = select_df.divi/select_df.trade/10*(10+select_df.shares)/10
 select_df = select_df.sort_values('divi_trade',ascending=False)
 select_df.to_csv('ts_test.result')
 print("write file done")

def select_share():
  df = pd.read_csv("today_all.csv")
  # 获取股价上涨超过9%的股票
  selected_codes = df[df['changepercent'] > 9][['code','name','changepercent']].sort_values('changepercent', ascending=False)
  # 遍历每支股票,下买单
  for item in selected_codes.iterrows():
    print(item[1]['code'],item[1]['name'])
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
if __name__ == '__main__':
  select_share()