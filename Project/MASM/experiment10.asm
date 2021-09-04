; 实验10
; 在8行3列，用绿色显示data段中以0为结尾的字符串
; dh 行号
; dl 列号
; cl 颜色（闪烁、背景颜色、高亮、字体颜色）
; b8000h---bffffh 用于显示 彩色字符
; 一个字节的显示占用两个字节，低字节存放数据，高字节存放颜色
; jcxz， 当cx=0时，执行，cx!=0时，穿透
; loop， 当cx=0时，穿透，cx!=0时，执行
assume cs:code
data segment
    db 'Welcome to masm!', 0            ; 16位字符串
data ends

stack segment
	db 16 dup(0)
stack ends

code segment
start:  mov dh, 8               ; 第8行 8*160 = 1280 = 500h
        mov dl, 8               ; 第 3 列与原有字符冲突，导致显示失败（显示失败与行数无关，与列数有关）（最低要从 8 开始）
        mov cl, 0fah               ; 颜色为绿色（背景为白色/黑色）（黑色：000 白色：111）
        mov ax, data
        mov ds, ax              ; 数据段地址初始化
        mov si, 0
        call show_str           ; 调用展示字符串的子程序
        mov ax, 4c00h           ; 结束指令
        int 21h
show_str:
        push ax                 ; 寄存器push暂存
        push si
        push dx                 ; push 与 pop 都只能对 16 位寄存器进行操作，无法操作8位寄存器
                                ; 子程序中使用的寄存器： ax, bx, cx, dx, es, ds, di, si,
        mov ax, 0b800h          ; 设置段地址
        mov es, ax              ; 设置段地址
        mov al, dh              ; 第 dh 行
        mov dl, 0a0h            ; 0a0h， 彩色字符显示区，每一行都是160个字节，也就是0a0h
        mul dl                  ; al * dl ---> dh * 160  定位行开始单元
        pop dx
        add al, dl              ; 定位从这行的第 dl 列开始
        mov bx, ax              ; 初始化 第 dh 行 第 dl 列的位置
        mov si, 0               ; si，用于定位data段中的数据
        mov di, 0               ; di，用于定位彩色字符显示区的内存单元
s:
        push cx
        mov ah, cl
        mov ch, 0
        mov cl, ds:[si]         ; 高位存颜色属性，低位存数据
        jcxz ok                 ; cx为0，不进行字符数据的处理，这里决定了要使用cx来进行字符数据的暂存
        mov es:[bx].di, cl      ; 注意 [bx].reg 是可行的
        mov es:[bx].di+1, ah    ; [bx].reg+idata 也是可行的
        inc si                  ; 取下一个字符
        add di, 2
        pop cx
        jmp s                   ; 跳转到s，进行下一个字符的处理

ok:
        pop si                  ; 寄存器pop回退
        pop ax
        ret
code ends
end start

; 在8086CPU中，可以用于进行内存单元的寻址的寄存器只有 bx,si,di,bp 这四个而已