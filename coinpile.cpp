#include<iostream>
#include<cmath>
using namespace std;
int main(){
int t;
cin>>t;
while(t--){
int a,b; cin>>a>>b; 
if(a>=b){
int x=abs(a-b);
a-=2*x;
b-=x;
if(a==b && a>=0  && a%3==0) cout<<"YES\n";
else cout<<"NO\n";
}
else{
int x=abs(a-b);
b-=2*x; a-=x;
if(a==b && a>=0 && a%3==0) cout<<"YES\n";
else cout<<"NO\n";
}
}
return 0;
}
 
