# @Author  Wangtianyv
# @date  2023/7/19 下午 04:21
# @version  1.0
import traceback
from common.common_Driver import ComDiver
from configs.env import Env
from utlis.handle_loguru import log
from utlis.handle_yaml import get_yaml
from utlis.handle_path import GetPath
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class BasePage:
    def __init__(self):
        self.driver = ComDiver().get_com_driver()
        self.locators = get_yaml(GetPath.configs_path/'allElements.yaml')[self.__class__.__name__]
        for key,value in self.locators.items():
            setattr(self,key,value)
    def get_element(self,locator,time = Env.TIMEOUT,sleep = Env.LUNXUNTIME,ass =True):
        try:
            if ass:
                return WebDriverWait(self.driver,time,sleep).until(ec.visibility_of_element_located(locator))
            return WebDriverWait(self.driver,time,sleep).until(ec.visibility_of_all_elements_located(locator))
        except:
            self.driver.get_screenshot_as_file(GetPath().img_path)
            log.error(f'获取element对象失败{traceback.format_exc()}')
    #打开网址
    def open_url(self,url):
        self.driver.get(url)
    #获取当前页url
    def get_url(self):
        return self.driver.current_url
    #获取当前页标题
    def get_title(self):
        return self.driver.title
    #点击
    def click_element(self,locator):
        return self.get_element(locator).click()
    #清除
    def clear_element(self,locator):
        return self.get_element(locator).clear()
    #需要时先清除在输入
    def input_element(self,locator,send,cle = False):
        if cle:
            self.clear_element(locator)
            self.get_element(locator).send_keys(send)
        else:
            self.get_element(locator).send_keys(send)
    #获取元素定位的text
    def get_text(self,locator):
        return self.get_element(locator).text
    #切换窗口
    def hand_title(self,title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if title in self.driver.title:
                break


