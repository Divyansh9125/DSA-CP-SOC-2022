#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
const ll m=1e9+7;
const int num=1e6*2;
vector<ll>fact(num+1,0);
vector<ll>inv(num+1,0); 
ll exponent(int base,int exp)
{
    if(exp==0)
    return 1;
    ll res=exponent(base,exp/2);
    if(exp%2==1)
    return (((res*res)%m)*base)%m;
    else
    return (res*res)%m;
}
void fact_inv()
{
    fact[0]=1;
    for(int i=1;i<=num;i++)
    fact[i]=(i*fact[i-1])%m;
    inv[num]=exponent(fact[num],m-2);
    for(int i=num-1;i>=0;i--)
    inv[i]=(inv[i+1]*(i+1))%m; 
}
int binomial(int n,int r)
{    
    return (((fact[n]*inv[n-r])%m)*inv[r])%m; 
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m;
    cin>>n>>m;
    fact_inv();
    cout<<binomial(n+m-1,n-1)<<"\n"; //Result of Beggar's Method
    return 0;
}