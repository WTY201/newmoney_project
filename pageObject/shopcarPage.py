# @Author  Wangtianyv
# @date  2023/7/28 下午 03:46
# @version  1.0
from common.basePage import BasePage
from ordersPage import ordersPage
class shopcarPage(BasePage):
    def add_shop(self):#添加商品
        self.click_element(self.car_plus)
    def del_shop(self):#减少商品
        self.click_element(self.car_minus)
    def go_to_orders(self):#结算
        self.click_element(self.submits)
        return ordersPage()#进入订单页
    #清除购物车
    def del_shopcar(self):
        self.click_element(self.all_shopcart)
        self.click_element(self.clear_shopcart)
        self.click_element(self.shop_main)
        return self

