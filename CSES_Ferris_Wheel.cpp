#include <iostream>
#include <algorithm>
using namespace std;

int result(int a[],int n,int x)
{
    sort(a,a+n);
    int i=0,j=n-1,count=0;
    while(i<j)
    {
        if(a[i]+a[j]>x)
        {
            count++;
            j--;
        }
        else
        {
            count++;
            i++;
            j--;
        }
        if(i==j)
        count++;
    }
    return count;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,x;
    cin>>n>>x;
    int a[n];
    for(int i=0;i<n;i++)
    cin>>a[i];
    cout<<result(a,n,x)<<"\n";
    return 0;
}