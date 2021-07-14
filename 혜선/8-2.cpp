#include <iostream>
#include <algorithm>

using namespace std;

int Answer;

bool compare(int a, int b){
    return a>b;
}

int main(int argc, char** argv){
    int T, test_case;
    int N, K;

    cin>>T;
    for (test_case = 0; test_case < T; test_case++){

        Answer=0;

        //과목의 수 N와 정우가 공부할 수 있는 과목의 수 K 입력받아
        cin>>N>>K;

        //N개의 점수를 담을 수 있는 공간 생성하여 N개의 점수를 입력받아
        int * scores = new int[N];
        for (int i=0 ; i<N ; i++)
            cin>>scores[i];
        
        //sort function을 사용하여 내림차순으로 정렬
        sort(scores,scores+N,compare);

        //내림차순으로 정렬된 원소 중 앞에서부터 K개 뽑아서 Answer에 더해
        for (int i=0 ; i<K ;i++){
            Answer+=scores[i];
        }

        cout << "Case #" << test_case + 1 << endl;
        cout << Answer << endl;
        delete[] scores;
    }

    return 0;
}