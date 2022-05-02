#include <iostream>
using namespace std;

typedef long long ll;
const ll m=1e9+7;
ll exponent(ll base,ll exp)
{
    if(exp==0)
    return 1;
    ll res=exponent(base,exp/2);
    if(exp%2==1)
    return (((res*res)%m)*base)%m;
    else
    return (res*res)%m;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    ll a,b;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        cin>>a>>b;
        cout<<exponent(a,b)<<"\n";
    }
    return 0;
}