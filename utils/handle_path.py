# @Author  Wangtianyv
# @date  2023/6/9 上午 09:42
# @version  1.0
#文件路径
import os
import time
from os.path import join
from glob import glob
from pathlib import Path
from pprint import pp
class GetPath:
    pjp = Path(__file__).parent.parent
    pro_date = pjp /'testData'
    #测试用例数据
    test_yaml = pro_date / 'login_fail.yaml'
    pgp = pjp / 'outFiles' / 'img'
    configs_path = pjp / 'configs'
    #log路径
    log_path = pjp / 'outFiles'/'log'
    data_path =pjp / 'data'
    #report路径
    repot_path = pjp /  r'outFiles\report\tmp'

    pat = f'cx{time.strftime("%Y%m%d-%H%M%S")}.png'
    #报错截图路径
    img_path = pgp / pat

if __name__ == '__main__':
    a= GetPath()
    print(a.img_path)
