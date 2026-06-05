#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    cin >> N >> M;
    
    vector<int> building;
    for(int i=0; i<N; i++){
        int tmp; 
        cin >> tmp;
        building.push_back(tmp);
    }
    for(int _=0; _<M; _++){
        int f; cin >> f;
        int move[2] = {1, -1};
        int target_high = building[f];
        
        int MIN_N = 1e9;

        int L_min=9999999, R_min=999999; 

        for(int R = f+1; R < N; R++){
            R_min = R-f;
            if(building[R] >= target_high){
                break;
            }
        }
        for(int L = f-1; 0 <= L; L--){
            L_min = f-L;
            if(building[L] >= target_high){
                break;
            }            
        }
        cout << min(R_min, L_min) << " ";
        //cout << R_min << L_min << " ";
    }

    return 0;

    
}