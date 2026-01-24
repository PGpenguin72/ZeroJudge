#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int a, b, mx = 0;
    int result[7] = {0};
    cin >> a;
    int ls[1000] = {0};
    for(int c = 0; c<a; c++){
        cin >> ls[c];
    }
    for(int i = 0; i<a; i++){
        result[ls[i]] += 1;
        if(ls[i]){
            mx += 1;
        }
    }
    int p = (result[0]-mx);
    if(p>=0){
        result[6] = (59*mx + p*50);
    }
    else{
        result[6] = (abs(59*result[0]) + abs(20*p));
    }

    for(int j = 0; j<7; j++){
        cout << result[j] << " ";
    }
    return 0;
}