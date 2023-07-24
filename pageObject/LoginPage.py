# @Author  Wangtianyv
# @date  2023/7/19 下午 07:28
# @version  1.0
from configs.env import Env
from common.basePage import BasePage
from pageObject.mainPage import MainPage


class LoginPage(BasePage):
    def open_cxurl(self):
        self.open_url(url=Env.CX_URL)
        self.click_element(self.login_o)
        self.click_element(self.phone)
        return self
    def in_user_pwd(self,user,pwd):
        self.click_element(self.agreement)
        self.input_element(self.username,user)
        self.input_element(self.password,pwd)
        self.click_element(self.login_t)
        return MainPage
    def del_user_pwd(self):
        self.clear_element(self.username)
        self.clear_element(self.password)

if __name__ == '__main__':
    a = LoginPage()
    a.open_cxurl().in_user_pwd(*Env.WTYUP)