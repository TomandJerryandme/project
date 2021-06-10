; TITLE   ***HELLO,WORLD进阶程序之选择分支 BY LLUCT***

DATA    SEGMENT   ;定义数据段
MSG1    DB      '***WELCOME TO MY PROGRAM BY LLUCT***','$'

;定义输出的第一个字符串信息,字符串必须用DB定义,$为结束标志
MSG2    DB      '1:BASIC MESSAGE 2:ADVANCED MESSAGE','$'

;定义输出的字符串信息:选择菜单
MSG3    DB      'PLEASE CHOOSE:','$'

;定义输出的字符串信息:选择前缀
MSG4    DB      'HELLO,WORLD!^-^','$'

;定义输出的字符串信息:分支1的信息
MSG5    DB      'THIS IS MY FIRST ASM_86 PROGRAM! @^-^@','$'

;定义输出的字符串信息:分支2的信息
ERRMSG  DB      'CHOOSE ERROR! -_-b','$'

;定义输出的字符串信息:选择错误信息
DATA    ENDS   ;数据段结尾

CODE    SEGMENT   ;定义代码段

        ASSUME  CS:CODE  ;规定CS的内容
        ASSUME  DS:DATA  ;规定DS的内容

START:  
        MOV     AX, DATA  ;程序从START开始
        MOV     DS, AX  ;DS置初值,DATA的段地址
        CALL ENTER  ;调用显示回车换行子程序
        LEA     DX, MSG1  ;输出第一个字符串的偏移地址
        CALL DISPCHS  ;调用显示字符串子程序
        CALL    ENTER  ;调用显示回车换行子程序
        CALL    ENTER  ;这个...同上啊^-^
        LEA     DX, MSG2  ;输出第二个字符串的偏移地址
        CALL DISPCHS  ;调用显示字符串子程序

AGAIN:  
        CALL    ENTER  ;定义AGAIN标号.用于选择错误循环
        LEA     DX, MSG3  ;输出第三个字符串的偏移地址
        CALL DISPCHS  ;调用显示字符串子程序
        MOV     AH, 01H  ;调用1号功能:从键盘输入一个字符并回显
        INT     21H  ;完成输入回显
        CMP     AL, '1'  ;输入的字符和1相比较
        JE      BASICP  ;如果相等,转移到BASICP标号(JE=Jump if Equal)
        CMP     AL, '2'  ;输入的字符和2相比较             ||
        JE      ADVANP  ;如果相等,转移到ADVANP标号(JE=如果相等就转移)
        JMP     ERROR  ;否则就无条件转移到ERROR标号

EXIT:   
        MOV     AH,4CH  ;4C号功能调用:终止当前程序并返回调用程序
        INT     21H  ;返回DOS

BASICP: 
        CALL    ENTER  ; 什么,还要解释啊.晕-_-!!!
        LEA     DX,MSG4  ;输出第三个字符串的偏移地址
        CALL DISPCHS  ;调用显示字符串子程序
        CALL    ENTER  ;..........
        JMP     EXIT  ;无条件转移到EXIT标号

ADVANP: 
        CALL    ENTER  ;55555555
        LEA     DX,MSG5  ;解释了四次,应该懂了吧
        CALL DISPCHS  ;调用显示字符串子程序
        CALL    ENTER  ;再问就死给你看
        JMP     EXIT  ;无条件转移到EXIT标号

ERROR:  
        CALL    ENTER
        LEA     DX,ERRMSG ;输出选择错误信息
        CALL DISPCHS  ;调用显示字符串子程序
        MOV DL,07H  ;输出ASCII码的报警(响铃)控制符BEL(07H)

 CALL DISPCH  ;调用显示单个字符子程序

 CALL    ENTER

        JMP     AGAIN

DISPCH  PROC    NEAR  

        ; 显示单个字符子程序,NEAR说明子程序和主程序在同一个代码段中(现无主程序调用)
        MOV     AH,02H  ;2号功能调用:显示器输出字符
        INT     21H  ;完成输出显示
        RET   ;返回

DISPCH  ENDP   ;子程序结尾

ENTER   PROC    NEAR    ; 显示回车换行子程序
        MOV     DL,0DH  ;输出ASCII码的回车控制符CR(0DH)
        CALL    DISPCH  ;调用显示单个字符子程序
        MOV     DL,0AH  ;输出ASCII码的换行控制符LF(0AH)
        CALL    DISPCH  ;调用显示单个字符子程序
        RET   ;返回

ENTER   ENDP   ;子程序结尾

DISPCHS PROC NEAR

;显示字符串子程序,NEAR说明子程序和主程序在同一个代码段中(现无主程序调用)
 MOV AH,09H  ;9号功能调用:显示字符串
 INT 21H  ;完成输出显示
 RET

DISPCHS ENDP
CODE    ENDS   ;代码段结尾
END     START  ;结束汇编

;把以上代码复制到记事本等文本程序中,并保存.(如helloch.asm)

;编译:masm helloch.asm

;连接:link helloch.obj

;执行:helloch.exe
