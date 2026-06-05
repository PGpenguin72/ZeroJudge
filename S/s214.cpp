#include <bits/stdc++.h>
using namespace std;

struct Node{
    int x, y;
    int time;
    int id;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long long m, n, k, t;
    cin >> m >> n >> k >> t;
    vector<vector<long long>> data(m, vector<long long>(n));

    vector<pair<int, int>> start_pos(k + 1);


    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cin >> data[i][j];
            if (data[i][j] > 0){
                start_pos[data[i][j]] = {i, j};
            }
        }
    }
    queue<Node> q;

    vector<int> has_node(k+1, 1);

    for (int id = 1; id <= k; id++) {
        q.push({start_pos[id].first, start_pos[id].second, 0, id}); 
    }

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1}; 

    while (!q.empty()){
        Node curr = q.front();
        q.pop();

        if (curr.time == t) {
            continue; 
        }
        for (int i = 0; i < 4; i++) {
            int nx = curr.x + dx[i];
            int ny = curr.y + dy[i];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                if (data[nx][ny] == 0) {
                    data[nx][ny] = curr.id;
                    has_node[curr.id]++;
                    
                    q.push({nx, ny, curr.time +1, curr.id});
                }
            }
        }
    }
    
    for (int id=1; id <=k; id++){
        cout << has_node[id] << " ";
    }
    cout << "\n";
    return 0;
}