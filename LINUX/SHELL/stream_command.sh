#!/bin/bash

# 输入输出重定向
# echo 'this is input and output redirect' > ./LINUX/SHELL/1.txt
# 获取当前路径(sh运行时，命令行的当前路径)
CRTDIR=$(pwd)
echo "$CRTDIR"
echo '\rthis is input and output redirect add' >> "$CRTDIR/LINUX/SHELL/1.txt"