#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

int apartments(int a[],int b[],int n,int m,int k)
{
    sort(a,a+n);
    sort(b,b+m);
    int i=0,j=0,count=0;
    while(i<n)
    {
        while(j<m && b[j]<a[i]-k)
        j++;
        if(abs(a[i]-b[j])<=k)
        {
            count++;
            i++;
            j++;
        }
        else
        i++;
    }
    return count;
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m,k;
    cin>>n>>m>>k;
    int a[n],b[m];
    for(int i=0;i<n;i++)
    cin>>a[i];
    for(int i=0;i<m;i++)
    cin>>b[i];
    cout<<apartments(a,b,n,m,k)<<"\n";
    return 0;
}