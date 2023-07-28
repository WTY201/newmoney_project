# @Author  Wangtianyv
# @date  2023/7/19 下午 08:06
# @version  1.0
from common.basePage import BasePage
from configs.env import Env
from shoplistPage import shoplistPage
from shopcarPage import shopcarPage
class MainPage(BasePage):
    #前往商品首页
    def go_to_shop(self):
        self.click_element(self.shopping)
        self.hand_title(Env.SHOPPINGTITLE)
        return self
    #选择商品
    def add_shop(self,name):
        self.shop[1]=self.shop[1].format(name)
        self.click_element(self.shop)
        return shopcarPage()
    def gp_to_shoplist(self,s=2):#点击更多
        self.cxtadd[1] = self.cxtadd[1].format(s)
        self.click_element(self.cxtadd)
        return shoplistPage()#进入全部商品详细页
    #进入购物车
    def go_to_shopcar(self):
        self.click_element(self.shopcart)
        return shopcarPage()

if __name__ == '__main__':
    print(MainPage().shop[1].format('《财经媒体写作指南》'))