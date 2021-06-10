; 自己重写输出hello world， 中文会乱码
DATA    SEGMENT
    HELLO DB 'Hello World', '$'
    INPUT DB ?
DATA ENDS
CODE    SEGMENT
    ASSUME CS:CODE, DS:DATA
START:
    MOV AX, DATA
    MOV DS, AX
    MOV AH, 09H
    MOV DX, OFFSET HELLO
    INT 21H
    ; MOV DX, INPUT
    ; MOV AH, 01H
    ; INT 21H
    ; MOV DS, INPUT
    ; MOV AH, 09H
    ; INT 21H
    MOV AH, 4CH
    INT 21H
CODE    ENDS
END START