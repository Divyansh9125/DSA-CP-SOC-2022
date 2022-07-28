#include <iostream>
using namespace std;

void z_function(string s, int z[]) 
{
    int n = s.length();
    z[0]=0;
    for (int i = 1, l = 0, r = 0; i < n; i++) 
    {
        if (i <= r)
            z[i] = min (r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            z[i]++;
        if (i + z[i] - 1 > r)
            l = i, r = i + z[i] - 1;
    }
}

int main()
{
    string s;
    cin>>s;
    int n = s.length();
    int z[n]={0};
    z_function(s,z);
    for(int i=0;i<n;i++)
        if(i+z[i]==n)
            cout<<i<<" ";
    cout<<n;
}