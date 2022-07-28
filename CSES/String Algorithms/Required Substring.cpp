#include <iostream>
#include <vector>
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
    int n;
    string s;
    cin>>n>>s;
    vector<int> arr;
    for(int i = 1;i<=s.length();i++)
    {
        if(s.length()%i!=0) continue;
        int k = i;
        string test = s.substr(0,i);
        bool found = false;
        while(k<s.length())
        {
            if(s.substr(k,i)!=test)
            {
                found = true;
                k+=i;
                break;
            }
            k+=i;
        }
        if(!found) arr.push_back(i);
    }
    for(int i=0;)
}