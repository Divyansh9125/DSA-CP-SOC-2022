#include <iostream>
#include <math.h>
using namespace std;

int countDivisors(int n)
{
    int c=0;
    for(int i=2;i*i<=n;i++)
    {
        if(n%i==0)
        c++;
    }
    if((int)sqrt(n)*sqrt(n)==n)
    return 2*c+1;
    else
    return 2*c+2;
}
int main()
{
    int n,x;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        cin>>x;
        cout<<countDivisors(x)<<"\n";
    }
    return 0;
}