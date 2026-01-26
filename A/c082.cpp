#include <iostream>
#include <string>
using namespace std;
int lost[2500][2] = {};
int len = 0;
char directions[4] = {'E', 'S', 'W', 'N'};
struct Result { 
    int x;
    int y;
    int d;
};

int check(int x, int y, int a, int b){
    if ((x > a || x < 0) || (y > b | y < 0)){
        return 1;
    }
    else{
        return 0;
    }
}

int check_2(int x, int y){
    for(int i=0; i<len; i++){
        if(lost[i][0] == x && lost[i][1] == y){        
            return 0;    
        }
    }   
    return 1;
}

Result move(int x, int y, int d, int a, int b){
    int mv_list[4][2] = {{x+1, y}, {x, y-1}, {x-1, y}, {x, y+1}};
    int status = check(mv_list[d][0], mv_list[d][1], a, b);
    if (status){
        if (check_2(x, y)){
            lost[len][0] = x;
            lost[len][1] = y;
            len += 1;
            return {x, y, -1};
        }
        else{
            return {x, y, d};
        }
    }
    else{
        return {mv_list[d][0], mv_list[d][1], d};
    }
}

int main(){
    int a, b;
    cin >> a >> b;
    int x, y;
    while(cin >> x){
        cin >> y;
        char dt;
        cin >> dt; 
        int d;
        for(int di =0; di < 4; di++){
            if(dt == directions[di]){
                d = di;
                break;
            }
        }
        string str;
        cin >> str;
        char R = 'R', L = 'L', F = 'F';
        int d_t_2 = 0;
        for(int i=0; i < str.length(); i++){
            if(str[i] == R){
                d = (d+1)%4;
            }
            else if(str[i] == L){
                d = (d-1+4)%4;
            }
            else if(str[i] == F){
                Result res = move(x, y, d, a, b);
                int x_t = res.x;
                int y_t = res.y;
                int d_t = res.d;
                if(d_t == -1){
                    d_t_2 = -1;
                    cout << x << " " << y << " " << directions[d] << " LOST\n";
                    break;
                }
                else{
                    x = x_t, y = y_t, d = d_t; 
                }
            }
        }
        if(d_t_2 != -1){
            cout << x << " " << y << " " << directions[d] << "\n";
        }
    }
}