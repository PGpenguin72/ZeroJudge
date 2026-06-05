#include <bits/stdc++.h>
using namespace std;

int n;

void dfs(string s, int L, int R){
    if ( R > L || L > n){
        return;
    }
    if(L+R == n*2){
        cout << s << "\n";
    }

    s[L+R] = '(';
    dfs(s, L+1, R);
    s[L+R] = ')';
    dfs(s, L, R+1);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(cin >> n){
        string s(n*2, '_');
        dfs(s, 0, 0);
        cout << "\n";
    }
    return 0;
}