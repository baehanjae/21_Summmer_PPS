#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>

using namespace std;

vector<double> pbgood(101);  // double타입 벡터 생성, 101개 원소 0으로 초기화 
vector<double> pbbad(101);	// "

int main () {
    int N, init;  
    double gg, gb, bg, bb; // goodgood, goodbad, badgood, badbad 
    cin >> N >> init; // N일 값 입력 
    cin >> gg >> gb >> bg >> bb; // 다음 날이 좋은 날인지 나쁜 날인지 확률 입력 (소숫점 첫째자리까지) 
    
    if (init == 1){ // 싫은 날(1)일 경우 
        pbgood[0] = bg; 
        pbbad[0] = bb;
    }
    else{ // 좋은 날(0)일 경우 
        pbgood[0] = gg;
        pbbad[0] = gb;
    }
    
    for (int i = 1 ; i < N ; i++){ 
        pbgood[i] = pbgood[i-1] * gg + pbbad[i-1] * bg; // 전날 좋고 다음날 좋을 경우와 전날 나쁘고 다음날 좋을 경우                 
        pbbad[i] = pbgood[i-1] * gb+ pbbad[i-1] * bb; // 전날 좋고 다음날 나쁠 경우와 전날 나쁘고 다음날 나쁠 경우   
    }
    
    printf("%.0f\n%.0f", round(pbgood[N-1]*1000), round(pbbad[N-1]*1000));
    
    return 0;
}

/*
좋은 날 나쁜 날
https://www.acmicpc.net/problem/17211
*/ 
