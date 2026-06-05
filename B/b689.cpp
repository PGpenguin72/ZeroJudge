#include <bits/stdc++.h>
using namespace std;

const int MAXN = 25;
char grid[MAXN][MAXN];
int steps[MAXN][MAXN];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int MX = 0;
    int MX_x = 0;
    int MX_y = 0;
    int grid_x, grid_y;    
    int start_y = 0;
    int start_x = 0;

    cin >> grid_y >> grid_x;
    
    for(int i=0; i<grid_y; i++){
        for(int j=0; j<grid_x; j++){
            cin >> grid[i][j];
            if(grid[i][j] == '.' && (i == 0 || i == grid_y - 1 || j == 0 || j == grid_x - 1)){
                start_y = i;
                start_x = j;
            }
        }
    }

    int dir_y[4] = {1, -1, 0, 0};
    int dir_x[4] = {0, 0, 1, -1};
 
    steps[start_y][start_x] = 1;
    
    MX_y = start_y; 
    MX_x = start_x;

    queue<pair<int, int>> dot;
    dot.push({start_y, start_x});

    while(!dot.empty()){
        auto p = dot.front();
        dot.pop();
        int y = p.first;
        int x = p.second;
        
        for(int d=0; d<4; d++){
            int now_y = y + dir_y[d];
            int now_x = x + dir_x[d]; 
            
            if(now_x < 0 || now_x >= grid_x || now_y < 0 || now_y >= grid_y){ 
                continue;
            }
            if(grid[now_y][now_x] == '#'){
                continue;
            }
            if(steps[now_y][now_x] != 0){
                continue;
            }
            
            dot.push({now_y, now_x});
            steps[now_y][now_x] = steps[y][x] + 1;
            if(steps[now_y][now_x] > MX){
                MX = steps[now_y][now_x];
                MX_x = now_x;
                MX_y = now_y;
            }
        }
    }

    cout << MX_y + 1 << " " << MX_x + 1 << "\n";
    
    return 0;
}