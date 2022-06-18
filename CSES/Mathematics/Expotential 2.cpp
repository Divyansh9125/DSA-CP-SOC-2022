#include <iostream>
using namespace std;
long long lim = 1000000007;
long long exp(long long a, long long b, long long ed)
{

    long long res = 1;
    while(b>0)
    {
        if(b%2==1)
        {
            res = res*a%ed;
        }
        a=a*a%ed;
        b/=2;
    }
    return res;
}

int main()
{
    long n;
    cin>>n;
    long long a[n], b[n], c[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i]>>b[i]>>c[i];
    }
    for(int i=0;i<n;i++)
    {
        cout<<exp(a[i], exp(b[i], c[i], lim-1), lim)<<endl;
    }
}
