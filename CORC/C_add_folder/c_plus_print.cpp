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
    string size_str = "123456";         // 在这个语句中 "123456"是一个C语言字符串，并不是C++的字符串，只有赋值之后才会变成C++的字符串
    cout << "str_len = " << size_str.length() << endl;
    int x = 2, y = 3;
    cout << float(x / y);
    cout << "a\rb" << endl;
    return 0;
}

// C++ string类中的常用方法
/**
 * string类
 * append
 * assign
 * at
 * back
 * begin
 * c_str
 * capacity
 * cbegin
 * cend
 * clear
 * compare
 * copy
 * crbegin
 * crend
 * data
 * empty
 * end
 * erase
 * find
 * find_first_not_of
 * find_first_of
 * find_last_not_of
 * find_last_of
 * front
 * get_allocator
 * insert
 * length       size与length是同样的效果，在底层代码中时同样的取值逻辑，只不过size是c++特有，而length是从C语言里面继承下来的
 * size
 * replace
 * reserve
 * resize
 * rfind
 * substr
*/