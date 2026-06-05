#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    int the_min=1000;
    int the_max=0;
    int ans_1=0;
    int ans_2=0;

    for(int student=0; student<N; student++){
        vector<int> data(M);
        vector<int> x;
        for(int grade=0; grade<M; grade++){
            int tmp;
            cin >> tmp;
            data.push_back(tmp);

            if(grade == 0){
                continue;
            }
            else{
                x.push_back(data[grade-1] - data[grade]);
            }
        }
        
        int student_min = *min_element(data.begin(), data.end());
        int student_max = *min_element(data.begin(), data.end());

        if (the_min > student_min){
            the_min = student_min;
            ans_1 = student + 1;
        }
        if (the_max < student_max){
            the_max = student_max;
            ans_2 = student + 1;
        }
    }
    cout << ans_1 << "\n" << ans_2 << "\n";
}