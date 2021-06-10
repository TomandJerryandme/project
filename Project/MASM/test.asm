; 该文件可以运行,在汇编语言中，';'表示注释的起始位置，如果需要进行多行注释，可以在END后进行，END后的所有代码都不会被翻译
; *** segment中，segment表示定义一个段的起始，***表示你取的这个段的名称
; 数据段中，'$'是字符串的结束标志，如果没有会报错
; 如果'$'不是用在字符串中，而是用于与其他标号进行操作，则'$'表示当前地址
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



MOV AH，01H
INT 21H吧，这是从键盘输入一个字符功能。
MOV AH，09H
INT 21H是输出字符串功能，但是必须先把字符串的地址送到DX中，既
LEA DX，要输出的字符串名
MOV AH，09H
INT 21H