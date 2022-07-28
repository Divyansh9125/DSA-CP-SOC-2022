#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

int triee[1000005][26];
int endnode[1000005];
int counter=0;
int dp[5001];

void insert(string s)
{
    int cur = 0;
    for(int i =0; i<s.length();i++)
    {
        if(triee[cur][s[i]-'a']==0)
            triee[cur][s[i]-'a'] = ++counter;
        cur = triee[cur][s[i]-'a'];
    }
    endnode[cur]=1;
}

int solve(string s)
{
    int m = s.length();
    dp[m]=1;
    int mod = 1000000007;

    for(int i = m-1; i>=0;i--)
    {
        int cur=0, ans=0;
        for(int j = i; j<m;j++)
        {
            if(triee[cur][s[j]-'a']==0) break;
            cur = triee[cur][s[j]-'a'];
            if(endnode[cur])
                ans = (ans+dp[j+1]%mod)%mod;
        }
        dp[i]=ans;
    }
    return dp[0];
}

int main()
{
    string line;
    int k;
    cin>>line>>k;
    string word[k];
    for (int i = 0; i < k; i++)
    {
        cin>>word[i];
        insert(word[i]);
    }
    cout<<solve(line)<<" ";
}