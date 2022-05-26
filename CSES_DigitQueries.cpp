#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;
 
typedef long long ll;
void digitNumber(ll n)
{
    ll x;
    vector<ll> v;
    int i=1;
    while(true)
    {
        x=(pow(10,i)-pow(10,i-1))*i;
        i++;
        if(x<=pow(10,18))
        v.push_back(x);
        else
        break;
    }
    ll digits=0,sum=0;
    for(i=0;i<v.size();i++)
    {
        if(n<sum)
        {
            digits=i; 
            break;
        }
        sum+=v[i];
    }
    if(digits==0)
    digits=i; 
    ll d=n-sum+v[digits-1];
    ll q=d/digits;
    ll rem=d%digits;
    ll num=pow(10,digits-1)-1+q;
    if(rem!=0)
    {
        string s=to_string(num+1);
        cout<<s[rem-1]<<endl;
    }
    else
    cout<<(num%10)<<endl;
}
int main()
{
    int q;
    ll n;
    cin>>q;
    for(int i=1;i<=q;i++)
    {
        cin>>n;
        digitNumber(n);
    }
    return 0;
}