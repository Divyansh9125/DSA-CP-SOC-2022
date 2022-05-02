#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
const ll m=1e9+7;
const int num=1e6;
vector<ll>fact(num+1,0);
vector<ll>inv(num+1,0); //Inverse Factorial
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
    inv[i]=(inv[i+1]*(i+1))%m; // 1/(n-1)! = 1/n! * n
}
int binomial(int n,int r)
{    
    return (((fact[n]*inv[n-r])%m)*inv[r])%m; //This approach uses Fermat's Little Theorem
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,a,b;
    cin>>n;
    fact_inv();
    for(int i=1;i<=n;i++)
    {
        cin>>a>>b;
        cout<<binomial(a,b)<<"\n";
    }
    return 0;
}