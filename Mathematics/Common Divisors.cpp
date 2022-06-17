#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int m, int n)
{
    if(n==0) return m;
    else return gcd(n, m%n);
}

int main()
{
    long n;
    cin>>n;
    long x[n];
    for(int i=0; i<n; i++)
    {
        cin>>x[i];
    }
    while(n>1)
    {
        for(int i=0; i<n-1;i+=2)
        {
            x[i/2]=gcd(x[i], x[i+1]);
        }
        if(n%2==1) {x[n/2]=x[n-1]; n=n/2+1;}
        else n=n/2;
    }

    cout<<x[0];
}