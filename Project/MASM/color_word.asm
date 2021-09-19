assume cs:code
data segment
	db 'welcome to masm!'
	db 0FEh, 0a4h, 71h  ; 要求的三个颜色对应的16进制代码
data ends

stack segment
	db 16 dup(0)
	; 也可以是下面的定义法：
	; dw 8 dup(0)
stack ends

code segment

start:
		                                    ; 设置data段，以及ds:bx指向data段的第一个单元，
		                                    ; 即ds:[bx]的内容就是data段第一个单元的内容  
		mov ax, data
		mov ds, ax
		                                    ; 设置显示缓存区段
		mov ax, 0b800h                      ; 设置起始缓存
		mov es, ax
		                                    ;设置栈段
		mov ax, stack
		mov ss, ax
		mov sp, 10h                         ; 指向栈顶

		                                    ; 初始化三个寄存器
		mov bx, 780h                        ; 行 从12-14行（注意：从第1行开始计数）  ？为什么从780h开始（12*160 = 1920 = 780h）
		mov si, 10h                         ; 颜色的偏移量，三次循环
					                        ; 每次增加 1h 指向下一个颜色（注意：是 1h 而不是 10h）

		mov cx, 3                           ; 三次循环改变行
	s: 	mov ah, ds:[si]                     ; 颜色事先存放在ah中
		push cx
		push si

		mov cx, 16                          ; 16次循环改变列

		mov si, 64                          ; 这里的si的意义是多少列, 
			                                ; 为什么从64列开始呢？
                                            ; (1)字符串为32字节，16字节ASCLL码，16字节属性
                                            ; (2)每一行有160列，那么余下有 160-32=128列为空白
                                            ;    要使得字符串居中显示，那么字符串的左边和右边
                                            ;  	都应该是64字节(128/2)，而列数是从0开始计数，
                                            ; 所以左边的64字节为0-63，所以这里偏移量为64
		mov di, 0

	s0:	mov al, ds:[di]                     ; 将date段中的字符一个一个传入es中
		mov es:[bx+si], al                  ; 低位存放字符
		mov es:[bx+si+1], ah                ; 高位存放颜色

		add si, 2                           ; 显示缓存区字符ASCII码偏移量为2
		add di, 1                           ; data段字符的偏移量，每次加 1 

		loop s0

		pop si
		pop cx                              ; 后进先出，先出栈si, 再出栈cx

		; add si, 1h                          ; 指向下一个颜色（增加 1h ，即为 + 1）
		inc si
		add bx, 0a0h                        ; 指向下一行 160=0a0h
		loop s

		mov ax, 4c00h
		int 21h
code ends

end start