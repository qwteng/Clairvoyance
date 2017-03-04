import  tushare as ts
import Clairvoyance as cl
stock_list = ts.get_st_classified()

print(cl.get_EXPMA(stock_list['code'], '2017-03-03', 'W'))
print(cl.get_EXPMA(['601918'], '2017-03-03', 'W'))
