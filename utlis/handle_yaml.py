# @Author  Wangtianyv
# @date  2023/6/9 上午 09:39
# @version  1.0
#读取yaml文件
import yaml
def get_yaml(yaml_file):
    with open(yaml_file,encoding='utf-8') as f:
        return yaml.safe_load(f.read())


