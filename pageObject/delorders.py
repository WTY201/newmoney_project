# @Author  Wangtianyv
# @date  2023/7/19 下午 08:52
# @version  1.0
#清除订单
from common.basePage import BasePage
class DelOrders(BasePage):
    def del_orders(self):
        try:
            self.click_element(self.order)
            self.click_element(self.del_order)
            self.driver.switch_to.alert.accept()
            self.click_element(self.del_l)
            self.driver.switch_to.alert.accept()
        except:
            return '无订单'
        else:
            return '订单已删除'
