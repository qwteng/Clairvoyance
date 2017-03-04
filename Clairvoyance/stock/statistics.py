# -*- coding:utf-8 -*-
"""
基于模型的统计接口
"""
import pandas as pd
import  tushare as ts

"""
根据股票代码列别、日期、K线类型，获取相应的历史数据。
date yyyy-mm-dd
kt: D日 W周
"""
def get_stcoks_data(codelist, date, kt):
    stock_data_list = []
    for code in codelist:
        stock_data = ts.get_hist_data(code, date, ktype=kt)
        stock_data['code'] = code
        stock_data_list.append(stock_data)
    df = pd.concat(stock_data_list)
    return df


# get the EXPMA of codelist
"""
根据股票代码列别、日期、K线类型，计算这些股票算术平均的涨跌幅。
date yyyy-mm-dd
kt: D日 W周
"""
def get_EXPMA(codelist, date, kt):
    df = get_stcoks_data(codelist, date,kt)
    num = len(df.index)
    if 0 == num :
        return 0
    sum = 0.0
    for change in df['p_change']:
        sum = sum + change
    return sum/num