# @Author  Wangtianyv
# @date  2023/7/19 下午 07:54
# @version  1.0
#初始化
from configs.env import Env
from pageObject.LoginPage import LoginPage
import pytest
from pageObject.delordersPage import DelOrders
@pytest.fixture(scope='session',autouse=True)
def starts_fixture():
    print('-----------------------------------测试用例开始---------------------------------')
    yield
    print('-----------------------------------测试用例结束----------------------------------')

@pytest.fixture(scope='session',autouse=False)
def sq_fixture():
    login = LoginPage()
    login.open_cxurl()
    main = login.in_user_pwd(*Env.WTYUP)
    print('登录成功')
    yield main
    print(DelOrders().del_orders())


