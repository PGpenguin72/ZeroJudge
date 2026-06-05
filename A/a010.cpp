#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int ip;
    cin >> ip;
    map<int,int> result;

    int last=1, num=0;
    int cnt;

    for(int i=2; i<(sqrt(ip)+1); i++){
        bool prime = true;

        for(int j=1; j<(sqrt(i)) ; j++){
            if(i%(j+1) == 0){
                prime = false;
            }
        }

        if(prime){
            cnt = 0;
            int tmp = ip;
            while(!(tmp%i)){
                cnt += 1;
                tmp /= i;
            }
            if(cnt){
                result[i] = cnt;
                num += 1;
                last = i;
            }
        }
    }

    if (num == 1){
        cnt = 0;
        while(!(ip%last)){
            cnt += 1;
            ip /= last;
        }
        if(cnt){
            if(ip != 1){
                result[ip] = cnt;
                num += 1;
                last = ip;
            }
        }
    }
    else if(!num){
        result[ip] = 1;
        last = ip;
    }

    if (!result.empty()) {
        auto last_it = prev(result.end());
        for (auto it = result.begin(); it != result.end(); ++it) {
            if (it->second != 1) {
                cout << it->first << "^" << it->second;
            } else {
                cout << it->first;
            }

            if (it != last_it) {
                cout << " * ";
            }
        }
        cout << "\n";
    }
    return 0;
}