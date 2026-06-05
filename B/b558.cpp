#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    while(cin >> n){
        cout << n*(n-1) /2 + 1 << "\n";
    }
    return 0;
}