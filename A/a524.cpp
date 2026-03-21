#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    while (cin >> n){
        string s;
        for (int i=0; i<n; i++){
            s.push_back('0' + n - i);
        }
        do{
            cout << s << "\n";
        } while (next_permutation(s.begin(), s.end(), greater<>()));
    }
    return 0;
}