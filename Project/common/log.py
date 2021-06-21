# -*- coding: utf-8 -*-
# python中logging的用法

import logging

_logging = logging.getLogger(__name__)
print(_logging.disabled)
# _logging.info("info")
_logging.warn("warn")
_logging.warning("warning")
_logging.debug("debug")
_logging.error("error")
