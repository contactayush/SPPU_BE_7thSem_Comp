#include <iostream>
using namespace std;
int steps=0;

int fibonacci_seris(int n){
    steps++;
    if(n==0){
        return 0;
    }

    if(n==1){
        return 1;
    }

    return fibonacci_seris(n-1)+fibonacci_seris(n-2);
}

int main(){
    int n;

    cout<<"Enter the the value of n:"<<endl;
    cin>>n;

    for(int i=0;i<=n;i++){
        int result=fibonacci_seris(i);

        cout<<result<<" ";
    }
    cout<<endl;

    cout<<"Total Steps:"<<steps<<endl;
}