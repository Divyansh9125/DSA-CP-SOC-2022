#include <iostream>
using namespace std;

int count(int x)
{
    int ans = 0;
    for(int i = 1; i*i<=x; i++)
    {
        if (x%i==0) ans+=2;
        if (i*i==x) ans--;
    }
    return ans;
}

int main()
{
    int n;
    cin>>n;
    int x[n];
    for(int i = 0; i<n; i++)
    {
        cin>>x[i];
    }
    for(int i = 0; i<n; i++)
    {
        cout<<count(x[i])<<endl;
    }
    return 0;
}