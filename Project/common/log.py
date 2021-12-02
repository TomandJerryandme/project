# python中logging的用法

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置

import os, sys
import logging
import threading

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, _NOTHING, DEFAULT = range(10)
LEVEL_COLOR_MAPPING = {
    logging.DEBUG: (BLUE, DEFAULT),
    logging.INFO: (GREEN, DEFAULT),
    logging.WARNING: (YELLOW, DEFAULT),
    logging.ERROR: (RED, DEFAULT),
    logging.CRITICAL: (WHITE, RED),
}

RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"
COLOR_PATTERN = "%s%s%%s%s" % (COLOR_SEQ, COLOR_SEQ, RESET_SEQ)


class DBFormatter(logging.Formatter):
    def format(self, record):
        record.pid = os.getpid()
        record.dbname = getattr(threading.current_thread(), 'dbname', '?')
        return logging.Formatter.format(self, record)

class ColoredFormatter(DBFormatter):
    # 当有log要显示的时候，会首先调用该方法对logger信息进行处理
    def format(self, record):
        fg_color, bg_color = LEVEL_COLOR_MAPPING.get(record.levelno, (GREEN, DEFAULT))
        record.levelname = COLOR_PATTERN % (30 + fg_color, 40 + bg_color, record.levelname)
        return DBFormatter.format(self, record)

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_LEVEL = logging.DEBUG

# logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置

def init_getlogger():
    """
        该函数只在调用的时候执行一次，进行logging的初始化工作
    """
    # getLogger(file_name)

    old_factory = logging.getLogRecordFactory()
    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        record.perf_info = ""
        return record
    logging.setLogRecordFactory(record_factory)
    logging.addLevelName(25, "INFO")
    # logging.captureWarnings(True)
    # logger = logging.getLogger()
    # logger.setLevel(LOG_LEVEL)

    format = '%(asctime)s pid:%(pid)s   %(levelname)s  dbname: %(dbname)s   name: %(name)s: msg: %(message)s  +=+=+  %(perf_info)s'
    handler = logging.StreamHandler()
    formatter = ColoredFormatter(format)
    # 因为在这里对handler进行了 formatter的赋值， 所以在有日志需要输出的时候，会调用 handler 中的formatter方法，找到 ColoredFormatter 的 format方法进行封装处理
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)
    # file_name = 'log.log'
    # header = logging.FileHandler('%s/db/%s' % (BASE_PATH, file_name))
    # header.setLevel(LOG_LEVEL)
    # file_format = logging.Formatter('%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')
    # header.setFormatter(file_format)
    # return logger

init_getlogger()

def get_log(name):
    return logging.getLogger(name)

# logging.basicConfig(level=log_level, format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S', filename='log.log', filemode='w')

'''
basicConfig 参数解析
filename: 指定日志存放的文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
%(levelno)s: 打印日志级别的数值9
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
'''