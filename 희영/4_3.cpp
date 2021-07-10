#include <iostream>

using namespace std;

int main(void) {
    int num=0, sum=0;
    int x[42] = {0}; // 나머지 값 0~41

    // 입력받은 숫자 10개를 42로 나누어서 해당 나머지 배열의 값을 1 증가 시킴.
    for(int i=0; i<10; i++){ 
        cin >> num;
        if(!x[num % 42]++){ // 해당 나머지 값의 배열이 0인 경우에만 sum의 값을 증가시킴.
            sum++; 
        }
    }
    cout << sum;
}