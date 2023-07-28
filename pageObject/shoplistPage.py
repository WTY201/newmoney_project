# @Author  Wangtianyv
# @date  2023/7/28 下午 03:39
# @version  1.0
from common.basePage import BasePage
from shopPage import shopPage
class shoplistPage(BasePage):
    def click_shop(self,ye,title):#输入商品页数，点击商品
        self.input_element(self.shu,f'{ye}\n')
        self.shop[1] = self.shop[1].format(title)
        self.click_element(self.shop)
        return shopPage()