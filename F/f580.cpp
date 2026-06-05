#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m; 
    cin >> n >> m;

    vector<int> dice = {1, 3, 5}; //現在點數, 後面點數, 左邊點數
    vector<vector<int>> dices(n, dice);

    for(int _=0 ; _<m ; _++){
        int temp_a, temp_b;
        cin >> temp_a >> temp_b;

        vector<int> temp_dice;
        if(temp_b > 0){
            temp_dice = dices[temp_a-1];
            dices[temp_a-1] = dices[temp_b-1];
            dices[temp_b-1] = temp_dice;
        }
        else if(temp_b == -1){ //向前轉
            temp_dice = dices[temp_a-1];
            vector<int> new_dice(3);

            new_dice[0] = temp_dice[1];
            new_dice[1] = 7 - temp_dice[0];
            new_dice[2] = temp_dice[2];

            dices[temp_a-1] = new_dice;
        }
        else if(temp_b == -2){ //向右轉
            temp_dice = dices[temp_a-1];
            vector<int> new_dice(3);
            
            new_dice[0] = temp_dice[2];
            new_dice[1] = temp_dice[1];
            new_dice[2] = 7 - temp_dice[0];

            dices[temp_a-1] = new_dice;
        }
    }
    for(int i=0 ; i<n; i++){
        cout << dices[i][0] << " ";
    }
    cout << "\n";
    return 0;
}