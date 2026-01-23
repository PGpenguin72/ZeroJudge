#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int a, b, c, pan;
    cin >> a >> b >> c;
    int result_a, result_b;
    pan = ((pow(b, 2) - 4*a*c));
    if (pan < 0){
        cout << "No real root";
        return 0;
    }
    result_a = (-b + sqrt(pan)) / (2*a);
    result_b = (-b - sqrt(pan)) / (2*a);
    if (result_a == result_b){
        cout << "Two same roots x=" << result_a;
    }
    else{
        cout << "Two different roots x1=" << result_a << " , x2=" << result_b;
    }
    return 0;
}