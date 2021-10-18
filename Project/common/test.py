import logging

from log import init_getlogger
# 进行logging的初始化，以后从logging中获取到的logger都适用这种格式
init_getlogger()

_logger = logging.getLogger(__name__)

_logger.error('this is a loggging error message')