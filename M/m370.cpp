#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int distance, n;
    cin >> distance >> n;
    
    vector<int> foods(n, 0);
    for(int i=0; i<n ; i++){
        cin >> foods[i];
    }

    sort(foods.begin(), foods.end());

    for(int i=0; i<n ; i++){
        if(foods[i] > distance){
            if(i >= (n+1)/2){
                cout << i << " " << foods[0] << "\n";
            }
            else{
                cout << n-i << " " << foods[n-1] << "\n";
            }
            break;
        }
        else if(foods[i] < distance && i == n-1){
            cout << n << " " << foods[0] << "\n";
        }
    }
    return 0;
}