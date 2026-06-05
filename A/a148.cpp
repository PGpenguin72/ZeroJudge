#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    while(cin >> n){
        int sum = 0;
        for(int j=0; j<n; j++){
            int tmp; cin >> tmp;
            sum += tmp;  
        }
        if(sum > 59*n){
            cout << "no\n";
        }
        else{
            cout << "yes\n";
        }
    }
    return 0;
}