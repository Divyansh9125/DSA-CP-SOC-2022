#include<iostream>
using namespace std;
int main(){
long long int n,x,m=0;
cin>>n;
long long a[n];
for(int i=0;i<n;i++)
cin>>a[i];
for(int i=1;i<n;i++){
x=a[i]-a[i-1];
if(x>=0) continue;
m=m-x;
a[i]=a[i-1];
}
cout<<m<<endl;
return 0;
}
