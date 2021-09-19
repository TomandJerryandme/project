# python中logging的用法

# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置


# python中logging的用法
import os, sys
import logging

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_LEVEL = logging.DEBUG
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置

def getlogger():
    # getLogger(file_name)
    logger = logging.getLogger()
    logger.setLevel(LOG_LEVEL)
    # file_name = 'log.log'
    # header = logging.FileHandler('%s/db/%s' % (BASE_PATH, file_name))
    # header.setLevel(LOG_LEVEL)
    # file_format = logging.Formatter('%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')
    # header.setFormatter(file_format)
    return logger


# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
# logging.info('this is a loggging info message')
# logging.debug('this is a loggging debug message')
# logging.warning('this is loggging a warning message')
# logging.error('this is an loggging error message')
# logging.critical('this is a loggging critical message')