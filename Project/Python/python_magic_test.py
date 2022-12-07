# 参考文档
# https://blog.csdn.net/wangjianno2/article/details/49050107
# 注： 在python中，一切都是对象，方法也是对象

class MagicClass(object):
    '''
        该类用于演示python的各种魔术变量与魔术方法
        并不是每个魔法方法都要实现，魔法方法定义后只是看该种对象对魔法方法的相关操作的响应而已
        对于一些对象，可能某些魔法方法根本用不到，可以不进行实现
        
        =============== 构造方法 start ===============
            __new__(cls, *)
            __init__(self, *)
            __del__(self)
        =============== 构造方法   end ===============

        =============== 单操作符 start ===============
            对象的一元操作符实现
            __pos__(self)
                对象的取正操作，如 int对象的取正操作 (-1)z.__pos__() = -1
            __neg__(self)
                对象的取负操作，如 int对象的取正操作 (-1)z.__neg__() = 1
            __abs__(self)
                对象的绝对值操作
            __invert__(self)
                对象的取反操作
            __round__(self, digits)
            __floor__(self)
            __ceil__(self)
            __trunc__(self)
        =============== 单操作符   end ===============
        
        =============== 访问控制 start ===============
            __getattr__(self, name)
            __setattr__(self, name)
            __delattr__(self, name)
            __getattribute__(self, name)
        =============== 访问控制   end ===============

        =============== 类的表示 start ===============
            __repr__()
                对象的显示
            __str__()
                对象转换为字符串时调用
            __unicode__(self)
            __format__(self)
            __hash__(self)
            __nonzero__(self)
            __dir__(self)
        =============== 类的表示   end ===============
        
        =============== 自定义序列 start ===============
            __len__(self)
            __getitem__(self, key)
            __setitem__(self, key)
            __delitem__(self, key)
            __iter__(self)
            __contains__(self, value)
            __reversed__(self)
            __missing__(self, key)
        =============== 自定义序列   end ===============

        =============== 上下文管理 start ===============
            __enter__(self)
            __exit__(self, exc, val, trace)
        =============== 上下文管理   end ===============

        =============== 拷贝 start ===============
            __copy__(self)
            __deepcopy(self, memodict)
        =============== 拷贝   end ===============

        =============== 比较操作符 start ===============
            __cmp__(self)
                对象的比较操作
            __eq__(self, other)
            __ne__(self, other)
            __lt__(self, other)
            __gt__(self, other)
            __le__(self, other)
            __ge__(self, other)
        =============== 比较操作符   end ===============

        =============== 算术操作符 start ===============
            __add__(self, other)
            __sub__(self, other)
            __mul__(self, other)
            __floordiv__(self, other)
            __div__(self, other)
            __truediv__(self, other)
            __mod__(self, other)
            __divmod__(self, other)
            __pow__
            __lshift__(self, other)
            __rshift__(self, other)
            __and__(self, other)
            __or__(self, other)
            __xor__(self, other)
        =============== 算术操作符   end ===============

        =============== 类型转换 start ===============
            __int__(self)
            __long__(self)
            __float__(self)
            __complex__(self)
            __oct__(self)
            __hex__(self)
            __index__(self)
            __trunc__(self)
            __coerce__(self)
        =============== 类型转换   end ===============

        =============== 描述符对象 start ===============
            __get__(self, instance, owner)
                定义当试图取出描述符的值时的行为
                instance 是拥有者类的实例
                owner 是拥有者类本身
            __set__(self, instance, owner)
                定义当描述符的值改变时的行为 
                instance 是拥有者类的实例
                value 是要赋给描述符的值
            __delete__(self, instance, owner)
                定义当描述符的值被删除时的行为 
                instance 是拥有者类的实例
        =============== 描述符对象   end ===============

        =============== 对象序列化 start ===============
            __getstate__(self)
            __setstate__(self)
            __reduce__(self)
        =============== 对象序列化   end ===============

        __call__(self, *)
            对象是否可调用
        __future__()
    '''

    def __new__(cls):
        pass

    def __init__(self):
        super().__init__()

    def __del__(self):
        pass

    def __copy__(self):
        # 复制时 复制的对象的定义
        pass

    def __call__(self, *kwargs):
        """
            该方法可以使对象像方法那样调用
            obj(*kwrags)
        """
        pass
    
    def __str__(self):
        print('调用了__str__方法')
        # __str__方法需要有返回值，并且必须是string类型
        return super(MagicClass, self).__str__()