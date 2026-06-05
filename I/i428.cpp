#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    int mx=0, mn=1e9;
    int last_x, last_y;
    cin >> n >> last_x >> last_y;
    for(int _=0; _ < n-1 ; _++){
        int x, y;
        cin >> x >> y;
        int d;
        d = abs(x-last_x) + abs(y-last_y);
        mx = max(d,mx);
        mn = min(d,mn);
        last_x = x;
        last_y = y;     
    }
    cout << mx << " " << mn << "\n";
    return 0;
}