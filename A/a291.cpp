#include <iostream>
using namespace std;

int main(){
    int a=0, b=0, c=0, d=0;
    while(cin >> a >> b >> c >> d){
        int n;
        cin >> n;
        for(int _=0 ; _<n ; _++){
            int ans[4] = {a, b, c, d};
            int e, f, g, h;
            cin >> e >> f >> g >> h;
            int cmp[4] = {e, f, g, h};
            int A=0, B=0, m=4;
            for(int j=0; j<4; j++){
                if (cmp[j] == ans[j]){
                    A += 1;
                    m -= 1;
                    ans[j] = -1;
                    cmp[j] = -2;
                }
            }
            for(int k=0; k < 4; k++){
                for(int l=0; l<4; l++){
                    if(cmp[k] == -2){
                        continue;
                    }
                    else if(cmp[k] == ans[l]){
                        B += 1;
                        ans[l] = -1;   
                        break;           
                    }
                }
            }
            cout << A << "A" << B << "B" << "\n";
        }
    }
    return 0;
}