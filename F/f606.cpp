#include <iostream>
using namespace std;

int main(){
    int n, m, k;
    cin >> n >> m >> k;
    int ls[50][50] = {{0}};
    for(int i=0; i < n; i++){
        for(int j=0; j < m; j++){
            cin >> ls[i][j];
        }
    }
    int citys[50][50];
    int min = 2e9;
    for(int plan=0; plan < k; plan++){
        int total[50][50] = {{0}};
        int tmp = 0;
        for(int server=0; server < n; server++){
            cin >> citys[plan][server];
            for(int city=0; city < m; city++){
                total[citys[plan][server]][city] += ls[server][city];
            }
        }
        for(int s=0; s < m; s++){
            for(int r=0; r < m; r++){
                if(s==r){
                   tmp += total[s][r];
                }
                else if(total[s][r] > 1000){
                    tmp += (total[s][r]-1000)*2 + 3000;
                }
                else{
                    tmp += total[s][r]*3;
                }
            }
        }
        if(tmp < min){
            min = tmp;
        }
    }
    cout << min;
    return 0;
}