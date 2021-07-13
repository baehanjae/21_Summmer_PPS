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
    
    while(!a.empty()){
        for ( int i=0 ; i<k-1 ; i++){
            a.push(a.front());
            a.pop();
        }

        if(1<a.size())
            cout<<a.front()<<", ";
        else
            cout<<a.front()<<">";
        a.pop();
    }
}