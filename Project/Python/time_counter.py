# -*- coding: utf-8 -*-

import time
from datetime import datetime
def time_counter(*out_args, **kwargs):
    # 最外层的类似装饰器，用于接受装饰器的参数
    time_multi = 0.001
    show_config = 'ms'
    if len(kwargs) and kwargs.get('show_config') == 's':
        # 没有传入参数
        show_config = 's'
        time_multi = 1
    def decorater_func_name_with_param(func_name):
        # 装饰器，用于接收被装饰的函数名
        # config_param: 秒/毫秒
        def any_thing(*args, **kwargs):
            # 装饰处理
            # begin_time = datetime.now()
            begin_time_time = time.time()
            func_name(*args, **kwargs)
            time.sleep(0.01)
            end_time_time = time.time()
            # end_time = datetime.now()
            # print("耗时： %s %s" % ((end_time - begin_time) / time_multi, show_config))
            print("耗时： %s %s" % ((end_time_time - begin_time_time) / time_multi, show_config))
        return any_thing
    return decorater_func_name_with_param

@time_counter('ms')
def say_hello(name):
    print("{Name} : Hello".format(Name=name))
