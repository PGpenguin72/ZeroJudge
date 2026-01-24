#include <iostream>
using namespace std;

int main(){
    int n = 0, m = 0;
    int ls[10000] = {0};
    cin >> n;
    cin >> m;
    for(int i=0; i < n; i++){
        cin >> ls[i];
    }
    int cmp[10000] = {0};
    for(int i=0; i < m; i++){
        cin >> cmp[i];
    }
    int tmp = 0;
    for(int j=0; j < n; j++){
        if(ls[j]!=cmp[tmp] && tmp){
            j = j - tmp;
            tmp = 0;
        }
        else if(ls[j]!=cmp[tmp]){
            tmp = 0;
        }
        else{
            tmp += 1;
        }
        if(tmp == m){
            cout << j - m + 2;
            return 0;
        }
    }
    cout << "not found";
    return 0;
}