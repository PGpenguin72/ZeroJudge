#include <iostream>
#include <math.h>
using namespace std;

int prime(int n){
    if (n == 1 | n == 0){
        return 0;
    }
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
    int x, y;
    while (cin >> x >> y){
        int mx =0;
        for(int j=x; j < y+1; j++){
            if (prime(j)){
                mx += 1;
            }
        }
        cout << mx << '\n';
    }
    return 0;
}