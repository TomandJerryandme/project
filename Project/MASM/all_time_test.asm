; 显示当前系统时间
assume cs:code
code segment
start:
    mov cx, 1                                   ; 因为下面用到了cx寄存器，所以会导致一直执行
s:
    ; 时
    mov al, 4                                   ; 从 CMOS RAM 中获取数据
    out 70h, al                                 ; 访问 70h 地址端口， 通知CMOS RAM 从 al 内存获取数据
    in al, 71h                                  ; 访问 71h 数据端口， 从 71h 端口中取得数据给 al

    mov ah, al                                  ; 对个位与十位数据分开处理，所以个位和十位都要有数据
    mov cl, 4                                   ; 
    shr ah, cl                                  ; 右移 4 位，将个位的数据排除
    and al, 00001111b                           ; and 00001111b 将十位的数据排除

    add ah, 30h                                 ; 分别计算 al 与 ah 中数字对应的 ascii 编码
    add al, 30h                                 ; 

    mov dh, 0eh                                 ; 对显示数据进行 显示格式的初始化
    mov bx, 0b800h                              ; 显示地址定位
    mov es, bx                                  ; 
    mov dl, ah                                  ; 使用 dx 进行数据传送，可以传送数据格式与数据值
    mov word ptr es:[160*12+40*2], dx
    mov dl, al
    mov word ptr es:[160*12+40*2+2], dx
    mov dx, 8e3ah
    mov word ptr es:[160*12+40*2+4], dx

    ; 分
    mov al, 2                                   ; 从 CMOS RAM 中获取数据
    out 70h, al                                 ; 访问 70h 地址端口， 通知CMOS RAM 从 al 内存获取数据
    in al, 71h                                  ; 访问 71h 数据端口， 从 71h 端口中取得数据给 al

    mov ah, al                                  ; 对个位与十位数据分开处理，所以个位和十位都要有数据
    mov cl, 4                                   ; 
    shr ah, cl                                  ; 右移 4 位，将个位的数据排除
    and al, 00001111b                           ; and 00001111b 将十位的数据排除

    add ah, 30h                                 ; 分别计算 al 与 ah 中数字对应的 ascii 编码
    add al, 30h                                 ; 

    mov dh, 0eh                                 ; 对显示数据进行 显示格式的初始化
    mov dl, ah                                  ; 使用 dx 进行数据传送，可以传送数据格式与数据值
    mov word ptr es:[160*12+40*2+6], dx
    mov dl, al
    mov word ptr es:[160*12+40*2+8], dx
    mov dx, 8e3ah
    mov word ptr es:[160*12+40*2+10], dx
    ; 秒
    mov al, 0                                   ; 从 CMOS RAM 中获取数据
    out 70h, al                                 ; 访问 70h 地址端口， 通知CMOS RAM 从 al 内存获取数据
    in al, 71h                                  ; 访问 71h 数据端口， 从 71h 端口中取得数据给 al

    mov ah, al                                  ; 对个位与十位数据分开处理，所以个位和十位都要有数据
    mov cl, 4                                   ; 
    shr ah, cl                                  ; 右移 4 位，将个位的数据排除
    and al, 00001111b                           ; and 00001111b 将十位的数据排除

    add ah, 30h                                 ; 分别计算 al 与 ah 中数字对应的 ascii 编码
    add al, 30h                                 ; 

    mov dh, 0eh                                 ; 对显示数据进行 显示格式的初始化
    mov dl, ah                                  ; 使用 dx 进行数据传送，可以传送数据格式与数据值
    mov word ptr es:[160*12+40*2+12], dx
    mov dl, al
    mov word ptr es:[160*12+40*2+14], dx

    jmp s
    mov ax, 4c00h
    int 21h

code ends
end start