#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b, total;
    total = 0;
    cin >> a >> b;
    for(int i=a; i<b+1; i++){
        if((i%4==0 and i%100 != 0)|| i%400 == 0){
            total += 1;
        }
    }
    cout << total;
    return 0;
}   
