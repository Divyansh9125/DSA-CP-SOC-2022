#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

typedef long long ll;
const ll m=1e9+7;

int dearrangement(int n)
{
    vector<ll> d(n+1);
    d[1]=0;
    for(int i=2;i<=n;i++)
    d[i]= (i*d[i-1]+ (i%2? -1:1))%m;
    return d[n];
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    cout<<dearrangement(n)<<"\n";
}