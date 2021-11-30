# include <iostream>
 using namespace std;
 int main(){
    string name;
    cout << "please input your name: " << endl;
    cin >> name;
    cout << "your \nname is " << name << "\n";
    // 垂直制表符 \v 相当于将原本的字符下移一行，但是前后位置不变
    // << endl; 等同于 << "\n";
    //  cout << "原来" << endl;
    //  system("pause");    // 作用 中断程序， 会显示  请按任意键继续...
     return 0;
 }