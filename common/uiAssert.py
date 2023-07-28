# @Author  Wangtianyv
# @date  2023/7/19 下午 04:22
# @version  1.0
import traceback
import pytest
from utils.handle_loguru import log
from utils.handle_path import GetPath
from common_Driver import ComDiver


class NewMoneyAssert:
    @classmethod
    def newmoneyassert(cls,result,condition,exp_result,msg='断言操做'):
        try:

            log_pass = '验证通过，预期结果{0}，实际结果{1}'
            assert_type = {'==': result == exp_result,
                           '!=': result != exp_result,
                           '>': result > exp_result,
                           '<': result < exp_result,
                           'in': str(result) in str(exp_result),
                           'not in': str(result) not in str(exp_result)}
            if condition in assert_type:
                with pytest.assume: assert assert_type[condition]
            else:
                raise AssertionError('断言错误')
            log.info(f'{msg},断言类型:{condition},断言结果:{log_pass.format(exp_result,result)}')
        except Exception as errore:
            log.error(f'断言错误------>{traceback.format_exc()}')
            ComDiver().get_com_driver().get_screenshot_as_file(GetPath.img_path)
            raise errore