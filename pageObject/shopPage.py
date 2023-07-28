# @Author  Wangtianyv
# @date  2023/7/28 下午 03:43
# @version  1.0
from common.basePage import BasePage
from ordersPage import ordersPage
from shopcarPage import shopcarPage
class shopPage(BasePage):
    def shop_add(self):#商品数量+1
        self.click_element(self.plus)
    def shop_del(self):#商品数量-1
        self.click_element(self.minus)
    def get_shopcar(self):#加入购物车
        self.click_element(self.add_shopcart)
    def get_shop(self):#立即购买
        self.click_element(self.buynow)
        return ordersPage()  #返回订单页
    def rmb_getshop(self):#rmb支付
        self.click_element(self,self.rmb)
    def dollar_getshop(self):#美元支付
        self.click_element(self.dollar)
    def go_to_shopcar(self):#前往购物车页
        self.click_element(self.shopcart)
        return shopcarPage() #返回购物车页