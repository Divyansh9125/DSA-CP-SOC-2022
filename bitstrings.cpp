#include<iostream>
#include<cmath>
using namespace std;
int main(){
int n;
cin>>n;
long long int x=1;
long long int y=pow(10,9)+7;
while(n>0){
x=x*2;
x=x%y;
n--;
}
cout<<x%y<<endl;
return 0;
}
