#include <iostream>

using namespace std;

int main(){
    cout << "please input a number: " << endl;
    int x;
    cin >> x;
    if (x % 7){
        cout << "NO" << endl;
    }else {
        cout << "YES" << endl;
    }
    return 0;
}