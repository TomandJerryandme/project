#!/bin/bash
# this is a note
read -p "输入网站名:" website

if test $website==1
then
	echo "test是验证类型的命令"
fi
if [ $website -eq 1 ]
then
	echo "你输入了1个字符"
	for var in 1 2 3 4
	do
		echo "$var、这是第$var个数字"
	done
else
	echo "你输入的网站名是 $website"
fi
exit 0
