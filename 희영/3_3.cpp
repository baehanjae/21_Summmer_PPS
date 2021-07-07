#include <iostream>
#include <string>
#include <cstring>

using namespace std;

// 'A' = 65, 'Z' = 90
int main() {
    char x[1000]; // 단어는 최대 1000자 이하
    cin >> x; // 입력받은 카이사르 암호
    int arr_size = strlen(x); // 입력받은 카이사르 암호의 길이
    
    // 입력받은 길이만큼 반복하면서, 해당 배열 index의 값을 3 줄인다.
    for(int i=0; i<arr_size; i++){ 
        x[i] = x[i]-3;
        // 만약, 3을 줄인 x[i]의 값이 65보다 작을 경우 26을 더한다.(대문자만 암호에 사용) 
        if(x[i]<65){
            x[i] = x[i]+26;
        }
    }

    cout << x; // 해독한 카이사르 암호를 출력한다.
    return 0;
}