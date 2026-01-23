#include <iostream>
using namespace std;

int main(){
    string ip;
    getline(cin, ip);
    for (int i; i < ip.size(); i++){
        cout << char(ip[i] -7);
    }
    return 0;
}