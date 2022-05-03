#include<iostream>
#include<cmath>
using namespace std;
int main(){
long long int n;
cin>>n;
long long int x,sum=0;
for(int i=0;i<n-1;i++){
cin>>x;
sum=sum+x;
}
long long int y=(n*(n+1)/2)-sum;
cout<<y;
}
