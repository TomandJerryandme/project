; 从控制台接收一个字符串并输出到控制台
DATA   SEGMENT
INPUT  DB  "Please input a string: ",'$'
OUTPUT DB  "Your input is: ",'$'
BUFFER DB  30				    ; 预定义20字节的空间， 但是只能输入19个字符
       DB  ?				    ; 待输入完成后，自动获得输入的字符个数
       DB  30  DUP(0)                  ; 不对该20个字节的空间内赋值？        DUP后面的括号里是变量的初始值
CRLF   DB  0AH, 0DH,'$'
DATA   ENDS
TACK  SEGMENT  STACK
       DW  30  DUP(0)
TACK  ENDS
CODE   SEGMENT
ASSUME CS:CODE, DS:DATA, SS:TACK
START:
        MOV AX, DATA
        MOV DS, AX                      
        LEA DX, INPUT                        ; 打印提示输入信息
        MOV AH, 09H
        INT 21H
        LEA DX,BUFFER                        ; 接收字符串
        MOV AH, 0AH
        INT 21H
        MOV AL, BUFFER+1                     ; 对字符串进行处理
        ADD AL, 2
        MOV AH, 0
        MOV SI, AX
        MOV BUFFER[SI], '$'
        LEA DX, CRLF                         ; 另取一行
        MOV AH, 09H
        INT 21H
        LEA DX, OUTPUT                       ; 打印提示输出信息
        MOV AH, 09H
        INT 21H
        LEA DX, BUFFER+2                     ; 输出输入的字符串
        MOV AH, 09H
        INT 21H
        LEA DX, CRLF                         ; 另取一行
        MOV AH, 09H
        INT 21H

        MOV AH, 4CH                          ; 返回DOS系统
        INT 21H
CODE   ENDS
END    START



汇编语言在数据段使用数据定义伪指令定义变量，对数据定义伪指令说明如下：
1、db（(byte，字节，一字节宽）
2、dw（word，字，两字节宽）
3、dd（double word，双字，四字节宽）
各个数据定义伪指令均可以连续定义变量。
示例如下：
DATAS SEGMENT;定义数据段
BUF0 DB 1     ; 定义一个字节型变量，名称是BUF0，初始值是01H
BUF1 DB "2"   ; 定义一个字符型变量，名称是BUF1，初始值是"2"
BUF2 DW 1     ; 定义一个字型变量，名称是BUF2，初始值是0001H
BUF3 DD 2     ; 定义一个双字型变量，名称是BUF3，初始值是00000002H
BUF4 DB 1 DUP(50)    ; 定义连续50个字节型变量，名称是BUF4，初始值是01H
BUF5 DB "12345678"   ; 定义一个字符型变量，名称是BUF5，初始值是"12345678"
DATAS ENDS    ; 数据段定义结束
STACKS SEGMENT       ; 定义堆栈段
DB 100 DUP(?)
STACKS ENDS
CODES SEGMENT        ; 定义代码段
ASSUME CS:CODES,DS:DATAS,SS:STACKS        ; 段寄存器关联
START:
MOV AX,DATAS
MOV DS,AX

CODES ENDS
END START



[指令语句]
每一条指令语句在源程序汇编时都要产生可供计算机执行的指令代码（即目标代码），所以这种语句又叫可执行语句。
每一条指令语句表示计算机具有的一个基本能力，如数据传送，两数相加或相减，移位等，
而这种能力是在目标程序（指令代码的有序集合）运行时完成的
是依赖于汁算机内的中央处理器（CPU）、存储器、I／O接口等硬件设备来实现的。

[伪指令语句]
伪指令语句是用于指示汇编程序如何汇编源程序，所以这种语句又叫命令语句。
例如源程序中的伪指令语句告诉汇编程序：该源程序如何分段，有哪些逻辑段在程序段中哪些是当前段，它们分别由哪个段寄存器指向；
定义了哪些数据，存储单元是如何分配的等等。伪指令语句除定义的具体数据要生成目标代码外，其他均没有对应的目标代码。
伪指令语句的这些命令功能是由汇编程序在汇编源程序时，通过执行一段程序来完成的，而不是在运行目标程序时实现的。