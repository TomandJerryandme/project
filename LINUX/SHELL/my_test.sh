#!/bin/bash

# https://www.runoob.com/linux/linux-shell-func.html
# 在powershell中输入命令 sh #    可以进入shell命令模式

function get_param()
{
    # 在shell的函数中，return和eval都可以用于返回值
    # 不能使用return来返回多个值，但可以使用eval来进行返回
    # 在字符串中如果要使用变量，字符串必须是使用双引号""括起来的，单引号不行
    eval $1="'This is x1'"
    eval $2="'This is x2'"
    eval $3="'This is x3'"
    echo "一共有 $# 个参数"
    echo "实参列表为  [$*]"
    if [ $4 ]
    then
        eval $4="'This is x4'"
    else
        echo "没有第四个参数"
    fi
}

# 这里可以
# x1=
# x2=
# x3=
# get_param x1 x2 x3
x1= x2= x3= x4=
# 在shell中，函数参数的传递使用以下的方式，不需要用()
get_param x1 x2 x3 x4
echo $x1
echo $x2
echo $x3
echo $x4