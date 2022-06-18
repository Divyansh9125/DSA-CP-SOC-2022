#include <iostream>
using namespace std;

void solve(long tower[], int n, long k)
{
    long num = k;
    int i = 0;
    int minind = -1;
    while(tower[i]!=0&&i<n)
    {
        if(minind==-1&&tower[i]>num)
            minind=i;
        else if(tower[i]>num && tower[minind]>tower[i])
            minind = i;
        i++;
    }
    if(minind==-1)
        tower[i]=num;
    else    
        tower[minind]=num;
}

int main()
{
    int n;
    cin>>n;
    long k[n], tower[n];
    for(int i = 0; i<n; i++)
    {
        cin>>k[i];
        tower[i]=0;
    }
    for(int i = 0; i<n; i++)
    {
        solve(tower, n, k[i]);
    }    
    int res = -1;
    for(int i = 0; i<n; i++)
    {
        if(tower[i]==0) 
        {
            res = i;
            break;
        }
    } 
    if(res==-1) cout<<n;
    else cout<<res;
}