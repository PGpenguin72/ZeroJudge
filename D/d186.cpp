#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    
    while(true){
        cin >> a >> b;
        int sum=0;
        if(a && b){
            for(int i=sqrt(a)-1; i< sqrt(b)+1; i++){
                int pw;
                pw = i*i;
                if(a<= pw && pw <= b){
                    sum ++;
                }
            }
            cout << sum << "\n";
        }
        else{
            break;
        }
    }
    return 0;
}