"""
计算购物车结算金额
定义一个函数 calculate_total 实现购物车总价核算，支持折扣优惠：
1. 形参设计：通过不定长参数 *prices 接收任意数量的商品单价；设置默认参数 discount 作为折扣比例，默认值为 0.9（九折）。
2. 运算逻辑：先累加所有商品价格，计算原价总金额；再结合折扣率核算优惠后价格。
3. 结果处理：最终金额统一保留两位小数，计算结果通过 return 返回。
"""
def calculate_total( *prices, discount = 0.9):
    total = sum(prices)
    final_price = total * discount
    return final_price
print(f"最终价格为：{round(calculate_total(10,25,45,66,81,16,58,44.25),2)}")
