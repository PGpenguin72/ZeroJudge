#include <bits/stdc++.h>
using namespace std;

long long cal(int a, int b, int c, int d, int e, int f, int i){
    return a*pow(i, 5)+b*pow(i, 4)+c*pow(i, 3)+d*pow(i, 2)+e*pow(i, 1)+f;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c, d, e, f, g;
    cin >> a >> b >> c >> d >> e >> f;
    if(a || b || c || d || e || f){
        bool status = true;
        for (int i=-35; i<= 35; i++){
            long long pan=0, tmp=0;
            pan = cal(a, b, c, d, e, f, i);
            tmp = cal(a, b, c, d, e, f, i+1);
            if(pan){
                if ((pan > 0 && tmp < 0) || (pan < 0 && tmp > 0)){
                    cout << i << " " << i+1 << "\n";
                    status = false;
                }
            }
            else{
                cout << i << " " << i << "\n";
                status = false;
            }
        }
        if(status){
            cout << "N0THING! >\\\\\\<\n";
        }
    }
    else{
        cout << "Too many... = =\"\n";
    }
    return 0;
}