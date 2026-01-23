#include <iostream>
#include <math.h>
using namespace std;

int prime(int n){
    if (n == 2){
        return 1;
    }
    if (n % 2 == 0){
        return 0;
    }
    int i = 3;
    while (pow(i, 2) <= n){
        if (n % i == 0){
            return 0;
        };
        i += 2;
    }
    return 1;
}

int main(){
    int x;
    while (cin >> x){
        if (prime(x)){
            cout << "質數\n";
        }
        else{
            cout << "非質數\n";
        }
    }
    return 0;
}