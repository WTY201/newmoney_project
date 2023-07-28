# @Author  Wangtianyv
# @date  2023/7/24 下午 05:16
# @version  1.0
import pytest

from pageObject.mainPage import MainPage
def test_rmb(shop_del_fixture:MainPage):
    main = shop_del_fixture
    #更多
    main.click_element(['xpath','//*[@href="https://mall.caixin.com/mall/web/list/list.html?type=127"]'])
    # 第2页
    main.input_element(['xpath','//*[@class="el-input__inner"]'],f'2\n')
    #选择商品
    main.add_shop('财新全网通VIP-1年（实体卡）')
    #选择人民币支付
    main.click_element(['xpath','//*[@value="人民币支付"]'])
    #添加进购物车
    # main.add_shopcar()
    main.click_element(['xpath','//*[@class="add-cart c-pointer"]'])
    #
    main.click_element(['xpath','//*[@class="right so-back-to-cart c-pointer"]'])
    main.put_shopcar(2)
    main.click_element(['id','ic-go-check-trigger'])
    q = main.get_text(['xpath','//*[@class="stringConcat  sclt-item-price-0"]'])

if __name__ == '__main__':
    # pytest.main([__file__,'-sv'])
    pytest.main(['-sv',__file__])