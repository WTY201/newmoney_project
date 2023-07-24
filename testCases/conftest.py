# @Author  Wangtianyv
# @date  2023/7/19 下午 07:54
# @version  1.0
#初始化
from pageObject.LoginPage import LoginPage
import pytest
@pytest.fixture(scope='session',autouse=True)
def starts_fixture():
    print('-----------------------------------测试用例开始---------------------------------')
    yield
    print('-----------------------------------测试用例结束----------------------------------')
@pytest.fixture(scope='session')
def login_fixture():
    login = LoginPage()
    login.open_cxurl()
    print('')
    yield login
    print()



