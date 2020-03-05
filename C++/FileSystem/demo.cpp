// 演示 C++ 中常用的一些函数
#include <iostream>
// stdio.h 引入 remove 函数
#include <cstdio>
// fstream 引入 ofstream
#include <fstream>
using namespace std;
int main(){
    // 删除文件: int remove(const char *pathname);
    // 可以删除文件、空的文件夹
    // 成功返回0，失败返回-1
    // std::cout << remove("./a") << endl;
    
    // 追加方式写文件
    ofstream outfile;
    outfile.open("./tmp.txt", ios::app);
    outfile << "hello world" << endl;
    outfile.close();
}

