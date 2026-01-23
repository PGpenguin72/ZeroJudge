#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    while (n){
        int ls[5] = {0};
        for (int i = 0; i < 4; i++){
            cin >> ls[i];
        }
        if (ls[1]-ls[0] == ls[3]-ls[2]){
            ls[4] = ls[3]*2-ls[2];
        }
        else{
            ls[4] = ls[3]*ls[3]/ls[2];
        }
        for (int j = 0; j < 5; j++){
            cout << ls[j] << " ";
        };
        cout << "\n";
        n -= 1;
    }
    return 0;
}