data    segment   ;定义数据段

input   db      100 dup(?)

;定义输入的字符串,字符串必须用db定义,长度为100个字节

msg1    db      'Hello,','$'

;定义输出的前缀字符串信息,字符串必须用db定义,$为结束标志(24h)

msg2    db      ',Welcome to here!','$'

;定义输出的后缀字符串信息

headmsg db      'PLEASE INPUT YOUR NAME:','$'

;开始显示的字符串信息

data    ends   ;数据段结尾

code    segment   ;定义代码段

        assume  cs:code  ;规定cs的内容

        assume  ds:data  ;规定ds的内容

start:  mov     ax,data  ;程序从start开始

        mov     ds,ax  ;ds置初值,data的段地址

        mov     si,0  ;变址寄存器置初值0

        call    enter  ;调用显示回车换行子程序

        lea     dx,headmsg ;输出开始显示的字符串的偏移地址

        call    dispchs  ;调用显示字符串子程序

repeat: mov     ah,01h  

;定义repeat标号,用于循环输入单个字符.调用1号功能:从键盘输入一个字符并回显

        int     21h  ;完成输入回显

        cmp     al,0dh  ;输入的字符和CR(回车)比较

        je      exit  ;如果等于回车就转移到exit

        mov     input[si],al ;把al的值传送到input的si地址中(好像是这样吧)

        inc     si  ;si加1

        jmp     repeat  ;无条件转移到repeat

exit:   call    enter

        mov     input[si],24h ;给输入完成的字符串加上结束标志($)

        call    enter  

        lea     dx,msg1  ;输出前缀字符串的偏移地址

        call    dispchs  ;调用显示字符串子程序

        lea     dx,input ;输出刚才输入的字符串

        call    dispchs  

        lea     dx,msg2

        call    dispchs

        call    enter

        mov     ah,4ch  ;4c号功能调用:终止当前程序并返回调用程序

        int     21h  ;返回dos

enter   proc    near  ;显示回车换行子程序

        mov     dl,0dh  ;输出ascii码的回车控制符cr(0dh)

        call    dispch  

        mov     dl,0ah  ;输出ascii码的换行控制符lf(0ah)

        call    dispch

        ret   ;返回

enter   endp   ;子程序结束

dispch  proc    near

        mov     ah,02h  ;2号功能调用:显示器输出字符

        int     21h  ;完成输出显示

        ret   ;返回

dispch  endp

dispchs proc    near

        mov     ah,09h  ;9号功能调用:显示字符串

        int     21h  ;完成输出显示

        ret   ;返回

dispchs endp

code    ends   ;代码段结尾

        end     start  ;结束汇编