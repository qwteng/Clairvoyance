import  tushare as ts
import Clairvoyance as cl
stock_list = ts.get_st_classified()
print(cl.get_EXPMA(['601918'], '2017-03-03', 'W'))
stock_list_st = stock_list['code']
stock_list_st03 = ['000962', '600230', '600725', '600721','000717','002109','000856','601918','600234','600603','002513','600301','000037','200037','002336']
print(cl.get_EXPMA(stock_list_st, '2017-03-03', 'W'))
print(cl.get_EXPMA(stock_list_st03, '2017-03-03', 'W'))