#include <stdio.h>

int main() {
    int a, b; 
    scanf("%d %d", &a, &b);
    
    int n;
    scanf("%d", &n);

    int item[n];
    for (int i=0; i < n ; i++){
        scanf("%d", &item[i]);
    }

    int sum = 0;
    
    for (int i=0; i<n ; i++){
        int m = item[i] % (a+b);

        if (m>=a){
            sum += (a+b)-m;
        }
    }
    printf("%d\n", sum);
    return 0;
}