# @Author  Wangtianyv
# @date  2023/7/28 下午 03:50
# @version  1.0
from common.basePage import BasePage
from addressPage import addressPage
from shopcarPage import shopcarPage
from payPage import payPage
class ordersPage(BasePage):
    def get_order(self,s=1):#提交订单
        self.xz_dress[1] = self.xz_dress.format(s)
        self.click_element(self.xz_dress)
        self.click_element(self.submits)
        return payPage()
    def new_address(self):#使用新地址
        self.click_element(self.address)
        return addressPage()
    def go_to_shopcar(self):#返回购物车
        self.click_element(self.shopcar)
        return shopcarPage()

