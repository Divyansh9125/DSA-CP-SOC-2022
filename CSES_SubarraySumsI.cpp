#include <iostream>
using namespace std;

int subSum(int arr[],int n,int x)
{
    int csum=arr[0],s=0,count=0;
    for(int e=1;e<n;e++)
    {
        csum+=arr[e];
        while(csum>x && s<e-1)
        {
            csum-=arr[s];
            s++;
        }
        if(csum==x)
        count++;
    }
    return count;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,x,count=0;
    cin>>n>>x;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
        if(arr[i]==x)
        count++;
    }
    cout<<subSum(arr,n,x)+count<<"\n";
    return 0;
}