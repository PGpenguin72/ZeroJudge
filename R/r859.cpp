#include <iostream>
using namespace std;

int main(){
    int usr[6] = {0};
    int prc[7] = {0};
    for(int i=0; i<6; i++){
        cin >> usr[i];
    }
    for(int i=0; i<7; i++){
        cin >> prc[i];
    }
    int ans = 0, spe = 0;
    for(int item=0; item<6; item++){
        for(int j=0; j<6; j++){
            if(usr[item] == prc[j]){
                ans += 1;
                break;
            }
        }
        if(usr[item] == prc[6]){
            spe = 1;
        }
    }
    string ans_ls[7] = {"X", "X", "X", "H", "E", "C", "A"};
    string spe_ls[6] = {"X", "X", "G", "F", "D", "B"};
    if(spe){
        cout << spe_ls[ans];
    }
    else{
        cout << ans_ls[ans];
    }
    return 0;
}