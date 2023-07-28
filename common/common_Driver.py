# @Author  Wangtianyv
# @date  2023/7/19 下午 04:21
# @version  1.0
import traceback
from selenium import webdriver
from configs.env import Env
from utils.handle_loguru import log
class Singleobj:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
class ComDiver(Singleobj):
    driver = None
    def get_com_driver(self, browse_type=Env.BROWSET_TYPE, headless_flag=Env.HEADLESS_FLAG):
        if self.driver is None:
            if headless_flag:
                if browse_type == 'chrome':
                    self.driver = webdriver.Chrome()
                elif browse_type == 'firefox':
                    self.driver = webdriver.Firefox()
            else:
                if browse_type == 'chrome':
                    option = webdriver.ChromeOptions()
                    option.add_argument('--headless')
                    self.driver = webdriver.Chrome(options=option)
                elif browse_type == 'firefox':
                    option = webdriver.FirefoxOptions()
                    option.add_argument('--headless')
                    self.driver = webdriver.Firefox(options=option)
            self.driver.maximize_window()  # 最大化窗口
            try:
                self.driver.set_page_load_timeout(Env.SET_PAGE_LOAD_TIMEOUT)  # 最大加载时间
            except :
                log.error(f'页面加载超过最大等待时间\n{traceback.format_exc()}')
        return self.driver