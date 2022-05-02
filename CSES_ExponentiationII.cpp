#include <iostream>
using namespace std;

typedef long long ll;
const ll m=1e9+7;
ll exponent(ll base,ll exp,ll m)
{
    if(exp==0)
    return 1;
    ll res=exponent(base,exp/2,m);
    if(exp%2==1)
    return (((res*res)%m)*base)%m;
    else
    return (res*res)%m;
}
// b^c = q(p-1)+r
// a^(b^c) = a^(q*(p-1))* a^r = (a^(p-1))^q * a^r
// By Fermat's Little Theorem, a^(p-1)=1(mod p)
// Therefore, a^(b^c) = a^r where r = b^c (mod p-1)
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,r;
    ll a,b,c;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        cin>>a>>b>>c;
        r=exponent(b,c,m-1);
        cout<<exponent(a,r,m)<<"\n";
    }
    return 0;
}