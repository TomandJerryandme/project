// #include "stdafx.h"

#include <iostream>
#include <cstring>
using namespace std;

int main(){
    // 注意，这里不能写成 cout << '123'; 
    // 在C与C++中，单引号引起来的表示一个字符
    // 双引号引起来表示字符数组，会默认在最后添加一个 \0 标志位 表示结束
    cout << "123" << 24 << "\tend" << endl;
    cout << strlen("xxxxx") << endl;
    return 0;
}