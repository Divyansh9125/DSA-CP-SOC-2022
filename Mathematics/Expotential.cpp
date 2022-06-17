#include <iostream>
using namespace std;
long long lim = 1000000007;
long long exp(long long a, long long b)
{
    long long res = 1;
    while(b>0)
    {
        if(b%2==1)
        {
            res = res*a%lim;
        }
        a=a*a%lim;
        b/=2;
    }
    return res;
}
int main()
{
    long n;
    cin>>n;
    long long a[n], b[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i]>>b[i];
    }
    for(int i=0;i<n;i++)
    {
        cout<<exp(a[i], b[i])<<endl;
    }
}
