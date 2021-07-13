#include <iostream>
#include <queue>

using namespace std;

int main(){
    queue <int> a;

    int n, k, i ;
    cin>>n;
    cin>>k;

    //1~n의 숫자를 차례로 큐에 넣어줌 
    for (int i=1 ; i<=n ; i++)
        a.push(i);
    cout<<"<";
    
    //큐가 비어있을 때까지 계속 실행 
    while(!a.empty()){
        
        //k의 배수 번째에 다다르기 전까는 큐의 front를 꺼내서 다시 큐의 마지막에 삽입
        for ( int i=0 ; i<k-1 ; i++){
            a.push(a.front());
            a.pop();
        }
        
        //k의 배수 번째는 출력 후 삭제 
        if(1<a.size())
            cout<<a.front()<<", ";
        else
            cout<<a.front()<<">";
        a.pop();
    }
}
