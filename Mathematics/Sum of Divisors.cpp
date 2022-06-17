#include <iostream>
using namespace std;

int main()
{
    long long n;
    cin>>n;
    long long res = 0;
    long long lim = 1000000007;
    long i;
    for(i = 1; i*i<n; i++)
    {
        if(n%i==0)
        {
            res = res + i + n/i;
            res = res%lim;
        }
    }
    if(i*i==n)
        res = (res+i)%lim;
    cout<<res;
}