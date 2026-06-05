#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    int raw_x, raw_y;
    cin >> raw_x >> raw_y;

    int raw_dx=raw_x, raw_dy=raw_y;
    int lef=0, rig=0, ret=0;

    for(int _; _<n-1; _++){
        int x, y;
        cin >> x >> y;
        int dx=x-raw_x, dy=y-raw_y;
        
        int cross = raw_dx*dy - raw_dy*dx;
        
        if (cross > 0){
            lef ++;
        }
        else if (cross < 0){
            rig ++;
        }
        else if ( (raw_dx > 0 && dx < 0) || (raw_dx < 0 && dx > 0) || (raw_dy > 0 && dy< 0) || (raw_dy < 0 && dy > 0) ){
            ret ++;
        }
        raw_x = x, raw_y =y;
        raw_dx = dx, raw_dy = dy;
    }
    cout << lef << " " << rig << " " << ret << "\n";
    return 0;
}