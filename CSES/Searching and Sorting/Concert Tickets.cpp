#include <iostream>
#include <algorithm>
using namespace std;

int finder(long arr[], int n, long flag)
{
    int lb = 0, ub = n-1, m = -1;
    bool found = false;
    while(lb<=ub)
    {
        int mid = (lb+ub)/2;
        if(arr[mid]==flag)
        {
            found = true;
            m = mid;
            break;
        }
        else if(arr[mid]>flag) ub = mid-1;
        else lb = mid+1;
    }
    if(!found)
    {
        m = ub;
    }
    return m;
}

int main()
{
    int n, m;
    cin>>n>>m;
    long h[n], t[m];
    for (int i = 0; i < n; i++)
    {
        cin>>h[i];
    }
    for (int i = 0; i < m; i++)
    {
        cin>>t[i];
    }
    
    sort(h, h+n);
    
    for (int i = 0; i < m; i++)
    {
        int c = finder(h, n, t[i]);
        if(c==-1) cout<<c<<" ";
        else
        {
            cout<<h[c]<<" ";
            h[c]=-1;
            n--;
        }
    }
}