#include <bits/stdc++.h>
using namespace std;

const int MAXN = 105;
int n;
char grid[MAXN][MAXN];
int steps[MAXN][MAXN];

int main(){
    ios::sync_with_stdio(false);
    cout.tie(nullptr);

    cin >> n;

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> grid[i][j];
        }
    }
    int start_y = 1;
    int start_x = 1;
    int end_y = n-2;
    int end_x = n-2;

    steps[start_y][start_x] = 1;

    queue<pair<int, int>> dot;
    dot.push({start_y, start_x});

    int dir_y[4] = {1, -1, 0, 0};
    int dir_x[4] = {0, 0, 1, -1};

    while(!dot.empty()){
        auto p = dot.front();
        dot.pop();
        int y = p.first;
        int x = p.second;

        if(x == end_x && y == end_y){
            break;
        }

        for(int d=0; d<4; d++){
            int now_y = y + dir_y[d];
            int now_x = x + dir_x[d];

            if(now_y < 0 || now_y >= n || now_x < 0 || now_x >= n){
                continue;
            }
            if(grid[now_y][now_x] == '#'){
                continue;
            }
            if(steps[now_y][now_x] != 0){
                continue;
            }

            steps[now_y][now_x] = steps[y][x] + 1;
            dot.push({now_y, now_x});
        }
    }

    if(steps[end_y][end_x] == 0){
        cout << "No solution!\n";
    }
    else{
        cout << steps[end_y][end_x] << "\n";
    }

    return 0;
}