#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int _=0; _ < t; _++){
        int n, p;
        int take_break[3650] = {0};
        int len = 0;
        cin >> n >> p;
        for(int party=0; party < p; party++){
            int ban;
            cin >> ban;
            for(int i=ban; i<n+1; i+=ban){
                if(i%7!=0 && i%7!=6){
                    int status=1;
                    for(int j=0; j<len ; j++){
                        if(take_break[j]==i){
                            status = 0;
                            break;
                        }
                    }
                    if(status){
                        take_break[len] = i;
                        len += 1;
                    }
                }
            }
        }
        cout << len << "\n";
    }
    return 0;
}