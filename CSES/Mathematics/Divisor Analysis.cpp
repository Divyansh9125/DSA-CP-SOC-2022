#include <iostream>
#include <math.h>
using namespace std;
long long exp(long long p, long long q)
{
    long long lim = 1000000007;
    long long res = 1;
    long long a = p, b = q;
    while(b>0)
    {
        if(b%2==1)
        {
            res = res*a%lim;
        }
        a=a*a%lim;
        b/=2;
    }
    return res%lim;
}
int main()
{
    int n;
    cin>>n;
    long x[n];
    long k[n];
    for(int i=0;i<n;i++)
    {
        cin>>x[i]>>k[i];
    }
    long long lim = 1000000007;
    long long num = 1, s = 1, p = 1;
    bool perfect = true;
    for(int i=0;i<n;i++)
    {
        if(k[i]%2==1) perfect = false;
        num = num*(k[i]+1)%lim;
        s = s * (long(round(pow(x[i], k[i]+1)))-1)/(x[i]-1)%lim;
        p = p * (exp(x[i], k[i]))%lim;
    }
    if(!perfect)
        p = exp(p, num/2);
    else
        p = exp(p, num);
    cout<<num<<endl<<s<<endl<<p;
}