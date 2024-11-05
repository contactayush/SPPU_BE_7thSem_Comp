#include <iostream>
#include <vector>
using namespace std;
int main(){
    int n;
    cout<<"Enter the value of n:"<<endl;
    cin>>n;

    vector<int> dp(n+1,-1);
    dp[0]=0;
    dp[1]=1;

    for(int i=2;i<=n;i++){
        dp[i]=dp[i-1]+dp[i-2];
    }

    for(int i=0;i<n;i++){
        cout<<dp[i]<<" ";
    }
  return 0;
}