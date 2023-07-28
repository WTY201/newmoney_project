# @Author  Wangtianyv
# @date  2023/7/19 下午 07:54
# @version  1.0
#初始化
import time

import pytest

from configs.env import Env
from pageObject.LoginPage import LoginPage
from pageObject.mainPage import MainPage
@pytest.fixture(scope='session')
def shop_del_fixture():
    login = LoginPage()
    login.open_cxurl()
    main = login.in_user_pwd(*Env.WTYUP)
    time.sleep(2)
    main.go_to_shop().del_shopcar()
    print('登录成功')
    print('清除购物车成功')
    yield main
    print('完成')



