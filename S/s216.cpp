#include <bits/stdc++.h>
using namespace std;

int main(){
    
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R; cin >> R;

    long long a=0, b=0, c=0;
    while(cin >> a >> b >> c){
        
        int p_a = a%2, p_b = b%2, p_c = c%2;
        if (p_a == p_b && p_b == p_c){
            cout << "A B C\n";
        }
        else if (p_a != p_b && p_a != p_c){
            cout << "A\n";
        }
        else if (p_b != p_a && p_b != p_c){
            cout << "B\n";
        }
        else{
            cout << "C\n";
        }
    }
    return 0;
}

