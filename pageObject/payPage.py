# @Author  Wangtianyv
# @date  2023/7/28 下午 04:27
# @version  1.0
from common.basePage import BasePage
class payPage(BasePage):
    def get_name(self):#商品名称
        return self.get_text(self.shop_name)
    def get_money(self):#商品金额
        return self.get_text(self.shop_money)