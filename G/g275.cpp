#include <bits/stdc++.h>
using namespace std;

int is_violate_A(vector<vector<int>> data){
    // A: 二四不同二六同：每一句第二、四個字必須不同平仄，而第二、六個字必須相同平仄
    for(int row=0; row < 2; row++)
    if(data[row][1] == data[row][3] || data[row][1] != data[row][5]){
        cout << "A";
        return 1;
    }
    return 0;
}

int is_violate_B(vector<vector<int>> data){
    // B: 仄起平收：第一句的結尾必須為仄聲，第二句的結尾必須為平聲
    if(data[0][6] == 0 || data[1][6] == 1){
        cout << "B";
        return 1;
    }
    return 0;
}

int is_violate_C(vector<vector<int>> data){
    // C: 上下相對：第一、二句的第二、四、六個字平仄必須不同
    if(data[0][1] == data[1][1] || data[0][3] == data[1][3] || data[0][5] == data[1][5]){
        cout << "C";
        return 1;
    }
    return 0;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int time; cin >> time;

    for(int i=0; i < time ; i++){
        vector<vector<int>> data(2, vector<int>(7));

        for(int j=0; j<2; j++){
            for(int k=0; k<7; k++){
                cin >> data[j][k];
            }
        }
        int is_violate; 
        is_violate = is_violate_A(data) + is_violate_B(data) + is_violate_C(data);

        if(is_violate){
            cout << "\n";
        }
        else{
            cout << "None\n";
        }
    }
}