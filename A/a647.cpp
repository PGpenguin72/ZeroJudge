#include <bits/stdc++.h>
using namespace std;

string dispose_or_keep(double ans_value){
    if(10.0 > ans_value && ans_value > -7.0){
        return "keep";
    }
    else{
        return "dispose";
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed << setprecision(2);

    int n;
    cin >> n;

    for(int _=0; _<n ; _++){
        int m, p;
        cin >> m >> p;

        double ans = ((p-m)*100.0)/m ;
        if(ans >0) ans += 0.0000001;
        else ans -= 0.0000001;

        if(0.005 > ans && ans > -0.005){
            ans = 0;
        }

        cout << ans << "%" << " " << dispose_or_keep(ans) << "\n";
    }

}