# coding=utf-8
import ccxt
from pprint import pprint
import time

# 火币的密钥
huoBi = ccxt.huobipro({
    'apiKey': 'dqnh6tvdf3-1592a8fc-728890ad-4d2e8',
    'secret': '2333e4d3-c07ff5aa-b00f3dc9-d275b',
})

# 获取XRP的价格
eosPrice = huoBi.fetch_ticker('EOS/USDT')['last']
print("当前价格XRP：", eosPrice)
balance = huoBi.fetch_balance()
usdtBalance = balance['USDT']['free']
print("余额USDT：",usdtBalance)

# 下单参数
order_symbol = 'EOS/USDT'  # 交易对
order_type = 'limit'  # 订单类型：限价单
order_side = 'buy'  # 下单方向
order_price = eosPrice - 0.01  # 下单价格 3.43
order_amount = 6 / eosPrice  # 下单数量  x

# 单个网格交易程序
# 下一个订单，循环监控订单状态，如果买单成交，则下一个买单，如果卖单成交，就下一个买单
takeOrder = huoBi.create_order(order_symbol, order_type, order_side, order_amount, order_price)  # 开始下单
takeOrder_id = takeOrder['id']  # 获得线上id
takeOrder_price = takeOrder['price']  # 获得线上订单价格
print("订单号：", takeOrder_id)
print("下单方向：", order_side)

while True:
    print("*****************")
    order_status = huoBi.fetch_order_status(takeOrder_id, order_symbol)  # 查询订单状态
    print("eos最新价格",eosPrice)
    print("当前订单状态：",order_status)
    if order_status == 'closed' and order_side == 'buy':
        order_side = 'sell'
        order_price = takeOrder_price + 0.01
        takeSellOrder = huoBi.create_order(order_symbol, order_type, order_side, order_amount, order_price)
        takeOrder_id = takeSellOrder['id']
        print("卖出的订单ID：", takeOrder_id)
        order_side = takeSellOrder['side']
        print(order_side)
        time.sleep(1.0)

    elif order_status == 'closed' and order_side == 'sell':
        order_side = 'buy'
        order_price = takeOrder_price - 0.01
        takeBuyOrder = huoBi.create_order(order_symbol, order_type, order_side, order_amount, order_price)
        takeOrder_id = takeBuyOrder['id']
        print("买入的订单ID：", takeOrder_id)
        order_side = takeBuyOrder['side']
        print(order_side)
    else:
        print("订单处于其他状态")
        time.sleep(1.0)
