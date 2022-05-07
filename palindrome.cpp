#include<iostream>
#include<cmath>
using namespace std;
bool ispalindrome(int x){
int reverse=0;
int temp=x;
while (temp!=0){
int newdigit=temp%10;
reverse=reverse*10+newdigit;
temp=temp/10;
}
return (x==reverse);
}
int main(){
    int x; cin>>x;
    cout<<ispalindrome(x);
}