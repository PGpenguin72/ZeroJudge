#include <bits/stdc++.h>
using namespace std;

int main(){
    long long h, m, s; cin >> h >> m >> s;
    long long h1, h2, m1, m2, s1, s2;
    s1 = s/60;
    s2 = s%60;
    m += s1;
    if(m < 0){
        m += 60;
        h -= 1;
    }
    m1 = m/60;
    m2 = m%60;
    h += m1;
    h1 = h/24;
    h2 = h%24;
    if(h2/10==0){
        cout << 0;
    }
    cout << h2 << ":";
    if(m2/10==0){
        cout << 0;
    }
    cout << m2 << ":";
    if(s2/10==0){
        cout << 0;
    }
    //cout << h << "" << m << "" << s;
    cout << s2 << "\n";
    return 0;
}