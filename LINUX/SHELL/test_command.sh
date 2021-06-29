# $? 仅对其上一条指令负责，一旦函数返回后其返回值没有立即保存入参数，那么其返回值将不再能通过 $? 获得
#shell 语言中 0 代表 true，0 以外的值代表 false
#!/bin/bash
function demoFun1(){
	echo "这是我的第一个 shell 函数!"
	return `expr 1 + 1`
}

demoFun1
echo $?

function demoFun2(){
	echo "这是我的第二个 shell 函数!"
	expr 1 + 3
}

demoFun2
echo $?
demoFun1
echo 在这里插入命令！
echo $?

# 在shell中无法使用变量接受函数返回值
# my_test=demoFun1()
# echo $my_test