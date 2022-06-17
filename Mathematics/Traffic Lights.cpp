#include <iostream>
#include <algorithm>
using namespace std;
long long n;
long long divide(long long gap, long long p, long long sorted[])
{
    long long loc = search(sorted, p), newgap = sorted[loc+1]-sorted[loc-1];

}

long long search(long long arr[], long long f)
{
    int lb = 0, ub = n-1, m = -1;
    while(lb<=ub)
    {
        int mid = (lb+ub)/2;
        if(arr[mid]==f)
        {
            m = mid;
            break;
        }
        else if(arr[mid]>f) ub = mid-1;
        else lb = mid+1;
    }
    return m;
}
int main()
{
    long long x;
    cin>>x>>n;
    long long p[n], sorted[n], ans[n];
    for(int i=0; i<n;i++)
    {
        cin>>p[i];
        sorted[i]=p[i];
    }
    sort(sorted, sorted+n);
    long long gap;
    for(int i=0; i<n-1;i++)
    {
        gap = max(gap, sorted[i+1]-sorted[i]);
    }
    long long num = n;
    for(int i = n-1; i>=n; i--)
    {
        ans[i] = gap;    
        divide(gap, p[i], sorted);
    }
    return 0;
}