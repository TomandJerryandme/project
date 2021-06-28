.386
DATA SEGMENT USE16
MESG DB 'HELLO WORLD', '$'
DATA ENDS
CODE SEGMENT USE16
    ASSUME CS:CODE, DS:DATA
BEG:
    MOV AX, DATA
    MOV DS, AX
    MOV AH, 9
    MOV DX, OFFSET MESG
    INT 21H         ; 这里到上面的所有指令，基本上都是为了输出字符串做准备; MOV AH, 9 INT 21H 是输出字符串的功能， MOV AH, 1   INT 21H 是输入字符串的功能
    MOV AH, 4CH
    INT 21H     ;bank to docs   调用中断21h的4ch号功能
CODE ENDS
END BEG




上述代码中有CODE代码段和DATA代码段
其作用大概如下：
区分同一段机器码对应的汇编语言指令
如：1000100111011000
上面这个机器码
数据：89D8H
指令：MOV AX, BX
如果没有分开代码段与数据段，就无法区分开这个机器码对应的不同意思，在编译汇编语言时就需要更多的机器码来区分
