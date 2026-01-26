#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, arr[3];
    cin >> n; 
    for(int i=1; i<=n; i++){
        cin >> arr[0] >> arr[1] >> arr[2];
        sort(arr, arr+3);
        cout << "Case " << i << ": "<< arr[1] << "\n";
    }
    return 0;
}