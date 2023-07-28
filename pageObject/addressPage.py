# @Author  Wangtianyv
# @date  2023/7/28 下午 03:56
# @version  1.0
from common.basePage import BasePage
from selenium.webdriver.support.ui import Select
from pageObject.ordersPage import ordersPage
class addressPage(BasePage):
    def get_address(self,shengji,shiji,qvji,sname,sphone,syb,cunji=None,):
        select = Select(self.get_element(self.sheng))#定位省级
        select.select_by_visible_text(shengji)
        select = Select(self.get_element(self.shi))#定位市级
        select.select_by_visible_text(shiji)
        select = Select(self.get_element(self.xian))#定位县级
        select.select_by_visible_text(qvji)
        if cunji != None:
            select = Select(self.get_element(self.cun))#定位村
            select.select_by_visible_text(cunji)
        self.input_element(self.name,sname)#输入收货人名字
        self.input_element(self.phone,sphone)#输入收货人手机号
        self.input_element(self.youbian,syb)#输入收货人邮编
        self.click_element(self.saveaddress)#保存地址
        return ordersPage()# 返回订单页

