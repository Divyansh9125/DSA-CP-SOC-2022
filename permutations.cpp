#include<iostream>
#include<cmath>
using namespace std;
int main(){
long long int n;
cin>>n;
if(n==1) cout<<1;
if(n==2||n==3) cout<<"NO SOLUTION";
if(n==4) cout<<"2 4 1 3";
if(n>4){
{for(int i=1;i<n+1;i=i+2) cout<<i<<" ";}
{for(int i=2;i<n+1;i=i+2) cout<<i<<" ";}
}
}