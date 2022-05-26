#include <iostream>
#include <math.h>
using namespace std;

typedef long long ll;
const ll modulo=10e9+7;

ll sumDiv(ll n)
{
    ll sum=0;
    for(ll i=1;i*i<n;i++)
    {
        if(n%i==0)
        {
            sum+=(i%modulo);
            sum+=((n/i)%modulo);
        }
    }
    if((ll)sqrt(n)*sqrt(n) ==n)
    return (sum+((ll)sqrt(n)%modulo)%modulo);
    else
    return sum%modulo;
}
int main()
{
    ll n,sum=0;
    cin>>n;
    for(ll i=1;i<=n;i++)
    sum+=(sumDiv(i)% modulo);
    cout<<(sum%modulo)<<"\n";
    return 0;
}