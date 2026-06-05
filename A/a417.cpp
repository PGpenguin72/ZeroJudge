#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    for(int _=0 ; _<t ; _++ ){
        int n=0, m=0;
        cin >> n >> m;

        vector<vector<int>> data(n, vector<int>(n, 0));

        int dir_y[4] = {0, 1, 0, -1};
        int dir_x[4] = {1, 0, -1, 0};
        
        int x=0, y=0;

        int dir, step;
        
        if (m==1){
            dir=0;
            step=1;
        }
        else{
            dir=3;
            step=3;
        }

        int cnt = 2;
        data[y][x] = 1;
        while(cnt <= n*n){
            int now_x = x + dir_x[dir], now_y = y + dir_y[dir];

            if(now_x < 0 || now_y < 0 || now_x >= n || now_y >= n){
                dir = (dir+step) % 4;
                continue;
            }

            if(data[now_y][now_x] != 0){
                dir = (dir+step) % 4;
                continue;
            }                    
            x = now_x, y = now_y;
            data[y][x] = cnt;
            cnt ++;
        };

        for(int i=0; i<n ; i++){
            for(int j=0; j<n ; j++){
                cout << setw(5) << data[i][j];
            }
            cout << "\n";
        }
        cout << "\n";
    }
    return 0;
}