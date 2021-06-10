; 汇编语言 借助dos 实现打开文件，读取文件内容输出到屏幕 然后关闭

SSEG SEGMENT
STACK DB 80H DUP(0)
SSEG ENDS
DSEG SEGMENT
ASKFN DB 'File Name: $'
FNAME DB 14,0,14DUP(?)
ERRMSG DB 'FILE ERROR! $'
BUFF DB 512 DUP(?)
DSEG ENDS
CSEG SEGMENT
ASSUME CS:CSEG,DS:DSEG,SS:SSEG
FILE PROC FAR
PUSH DS
XOR AX,AX
PUSH AX
MOV AX,DSEG
MOV DS,AX
LEA DX,ASKFN            ; 提示信息的首地址
MOV AH,09H
INT 21H                 ; 输出DS:DX指向的字符串（即提示信息）
LEA DX,FNAME;
MOV AH,0AH              ; 把键盘输入的字符存入缓冲区（即DS:DX），然后把实际输入的数量存入FNAME+1
INT 21H
MOV DL,0AH              ; 这是换行符
MOV AH,2                ; 输出DL的字符到屏幕
INT 21H
MOV BL,FNAME+1
MOV BH,0                ; 这里是为了把BL扩展到BX；
MOV [BX+FNAME+2],BH     ; 文件名的最后放上一个0,BX是文件名的长度
LEA DX,FNAME+2          ; 把文件名的首地址取给DX
MOV AX,3D00H            ; AH的3D是打开文件的功能，AL的内容是3种打开文件的格式，0=读，1=写，2=读和写
INT 21H                 ;
JC EXIT                 ; 如果文件打开出错的话跳转到EXIT
MOV BX,AX               ;
AGAIN:MOV CX,512        ; 每次读入的字节数
LEA DX,BUFF             ; 把缓冲区的偏移地址取给DX，这样就可以把文件内容读进DX
MOV AH,3FH              ; 读取文件内容，如果读到文件尾部，AX是0，否则是实际读入数
INT 21H
JC EXIT                 ; 如果打开出错了跳转
PUSH AX;
MOV CX,AX               ; 把实际读到的字节数给CX
MOV SI,OFFSET BUFF      ; 把缓存区首地址给SI，其实给哪个都可以，不限制
PUTC:
MOV DL,[SI]             ; 逐个输出
INC SI
MOV AH,2                ; 输出DL的字符到屏幕
INT 21H                 ; 
LOOP PUTC               ; 
POP AX                  ; 
CMP AX,512              ; 如果读到文件尾部，AX是0，否则是实际读入数
JE AGAIN                ; 只有两种可能一种是读完了，那么AX是0，不相等，还有一种可能是没读完，那AX就是512
MOV AH,3EH              ; 关闭文件
INT 21H                 ; 
RET
EXIT:LEA DX,ERRMSG
MOV AH,9
INT 21H                 ; 
RET                     ; 
MOV AH,4CH              ; 
INT 21H                 ; 
FILE ENDP
CSEG ENDS               ; 