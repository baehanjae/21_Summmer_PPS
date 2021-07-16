#include <iostream>
#include <queue>

using namespace std;

int main(){
	queue <int> a;
	int n, k, i;
	cin >> n ;
	cin >> k ;

	//1~n의 숫자를 차례로 큐에 넣어줌 
	for (i=1 ; i<=n ;i++)
	 	a.push(i);
	cout<<"<";
	i=1;
	while(n-1){
		// i 나누기 k의 나머지가 0이 아닐 때 front 값을 다시 큐에 넣고 기존 값은 pop
		if ( i % k !=0){
			a.push(a.front());
			a.pop();
		}
		// i 나누기 k의 나머지가 0일 때 front 값을 출력하고 pop
		else{
			cout << a.front() << ", ";
			a.pop();
			n--;
		}
		i++;
	}
	cout<<a.front()<<">";
	return 0;
}
