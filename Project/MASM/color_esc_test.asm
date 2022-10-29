; 在 屏幕上 依次输出 a-z, 按下 esc 键 变色

assume cs:code

stack segment
    db 128 dup (0)
    ; dup 有可能是调用了内核系统的 dup 函数，与之类似的还有 dup2 函数 内核系统的dup函数的作用，复制一个 打开的文件描述符 并返回， 二者指向同一个打开的文件句柄
stack ends

data segment
    dw 0, 0
data ends

code segment
start:
    mov ax, stack
    mov ss, ax
    mov sp, 128

    mov ax, data
    mov ds, ax
    
    mov ax, 0
    mov es, ax

    push es:[9*4]
    pop ds:[0]
    push es:[9*4+2]
    pop ds:[2]

    mov word ptr es:[9*4], offset int9
    mov es:[9*4+2], cs

    mov ax, 0b800h
    mov es, ax
    mov ah, 'a'

s:
    mov es:[160*12+40*2], ah
    call delay
    inc ah
    cmp ah, 'z'
    jna s

    mov ax, 0
    mov es, ax

    push ds:[0]
    pop es:[9*4]
    push ds:[2]
    pop es:[9*4+2]

    mov ah, 4ch
    int 21h

delay:
    push ax
    push dx
    mov dx, 10h
    mov ax, 0
s1:
    sub ax, 1
    sbb dx, 0
    cmp ax, 0
    jne s1
    cmp dx, 0
    jne s1
    pop dx
    pop ax
    ret

int9:
    push ax
    push bx
    push es

    in al, 60h

    pushf
    pushf
    pop bx
    and bh, 11111100b
    push bx
    popf
    call dword ptr ds:[0]

    cmp al, 1
    jne int9ret

    mov ax, 0b800h
    mov es, ax
    inc byte ptr es:[160*12+40*2+1]

int9ret:
    pop es
    pop bx
    pop ax
    iret

code ends
end start