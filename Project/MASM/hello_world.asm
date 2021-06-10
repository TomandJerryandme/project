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
