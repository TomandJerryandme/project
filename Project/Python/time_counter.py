# -*- coding: utf-8 -*-

import time
from datetime import datetime
def time_counter(*out_args, **kwargs):
    # 装饰器只能接收一个参数，并且还是函数类型, 所以需要一个最外层的装饰来接收参数, 然后返回一个装饰器
    # @后面必须是装饰器的实例，所以@time_counter之后，返回的是一个decorater_func_name_with_param装饰器实例
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
            print(func_name.__name__ + "耗时： %s %s" % ((end_time_time - begin_time_time) / time_multi, show_config))
        return any_thing
    return decorater_func_name_with_param

@time_counter('ms')
def say_hello(name):
    print("{Name} : Hello".format(Name=name))



def _round(value, persion_value):
    """
        精度转换
    """
    return round(value, persion_value)