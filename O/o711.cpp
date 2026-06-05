#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    
    int m1, m2, h1, h2;
    cin >> m1 >> m2 >> h1 >> h2;

    int a1 = m1 * m1;
    int a2 = m2 * m2;
    int v1 = a1 * h1;
    int v2 = a2 * h2;

    int h = 0;       
    int mx = 0;      
    int tot = 0;     

    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp; 
        int dh = 0; 

        tot += tmp; 

        if (tot <= v1) {

            dh = tmp / a1;
        } else {

            if (h <= h1) {

                int need_bottom = a1 * (h1 - h); 
                if (tmp <= need_bottom) {

                    dh = tmp / a1;
                } else {
                    int remain = tmp - need_bottom;
                    dh = (h1 - h) + remain / a2;
                }
            } else {

                dh = tmp / a2;
            }
            if (tot >= v1 + v2) {
                dh = h1 + h2 - h;
            }
        }

        h += dh;
        mx = max(mx, dh);
    }

    cout << mx << "\n";
    return 0;
}