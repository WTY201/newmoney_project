# @Author  Wangtianyv
# @date  2023/7/19 下午 08:06
# @version  1.0
from common.basePage import BasePage
from configs.env import Env
class MainPage(BasePage):
    def go_to_shop(self):
        self.click_element(self.shopping)
        self.hand_title(Env.SHOPPINGTITLE)
        return self
    def add_shop(self,name):
        self.shop[1]=self.shop[1].format(name)
        self.click_element(self.shop)
        return self
    def puls_l(self):
        self.click_element(self.plus)
    def mins_L(self):
        self.click_element(self.minus)
    def car_puls(self):
        self.click_element(self.car_plus)
    def car_mins(self):
        self.click_element(self.car_minus)
    def get_shop(self):
        self.click_element(self.buynow)
        self.click_element(self.submits)
    def add_shopcar(self):
        self.click_element(self.add_shopcart)
        self.click_element(self.submits)
    def del_shopcar(self):
        self.click_element(self.shopcart)
        self.click_element(self.all_shopcart)
        self.click_element(self.clear_shopcart)
        self.click_element(self.shop_main)
        return self

if __name__ == '__main__':
    print(MainPage().shop[1].format('《财经媒体写作指南》'))