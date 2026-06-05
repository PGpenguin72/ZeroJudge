#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    while(cin >> n && n != 0){
        int cnt=0;
        while(n &1){
            cnt ++;
            n >>= 1;
        }
        cout << cnt << "\n";
    }
    return 0;
}