import log
_logger = log.get_log(__name__)

class ValidationError(Exception):
    def __init__(self, name, value=None):
        # 异常的显示
        self.name = name
        self.value = value
        self.args = (name, value)