

#写入log文件
from configparser  import  ConfigParser
from loguru import logger
from utils.handle_path import GetPath
from time import strftime
import os
import logging
class PropogateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)

class MyLog():
    __instance = None  # 单例实现
    __call_flag = True  # 控制init调用，如果调用过就不再调用

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    # def __init__(self):
    def get_log(self):
        if self.__call_flag:  # 看是否调用过
            __curdate = strftime('%Y%m%d-%H%M%S')
            cfg = ConfigParser()
            cfg.read(os.path.join(GetPath().configs_path,'loguru.ini'), encoding='UTF-8')
            logger.remove(handler_id=None)  # 关闭console输出
            logger.add(os.path.join(GetPath().log_path,'cx') + __curdate + '.log', encoding='utf8', # 日志存放位置
                       retention=cfg.get('log', 'retention'),  # 清理
                       rotation=cfg.get('log', 'rotation'),  # 循环 达到指定大小后建立新的日志
                       format=cfg.get('log', 'format'),  # 日志输出格式
                       compression=cfg.get('log', 'compression'),  # 日志压缩格式
                       level=cfg.get('log', 'level'))  # 日志级别
            logger.add(PropogateHandler())
            self.__call_flag = False  # 如果调用过就置为False
        return logger

log = MyLog().get_log()
if __name__ == '__main__':
    log.error('testing')

