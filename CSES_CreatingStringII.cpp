#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
const ll m=1e9+7;
const int num=1e6;
vector<ll>fact(num+1,0);
vector<ll>inv(num+1,0); 
ll exponent(int base,int exp)
{
    if(exp==0)
    return 1;
    ll res=exponent(base,exp/2);
    if(exp%2==1)
    return (((res*res)%m)*base)%m;
    else
    return (res*res)%m;
}
void fact_inv()
{
    fact[0]=1;
    for(int i=1;i<=num;i++)
    fact[i]=(i*fact[i-1])%m;
    inv[num]=exponent(fact[num],m-2);
    for(int i=num-1;i>=0;i--)
    inv[i]=(inv[i+1]*(i+1))%m; 
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    fact_inv();
    string s;
    cin>>s;
    int l=s.length(),res=fact[l]%m;
    vector<int> v(27,0);
    for(int i=0;i<l;i++)
    v[s.at(i)-96]++;
    for(int i=1;i<27;i++)
    res=(res*inv[v[i]])%m;
    cout<<res<<"\n";
    
}