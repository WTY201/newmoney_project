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


if __name__ == '__main__':
    print(MainPage().shop[1].format('《财经媒体写作指南》'))