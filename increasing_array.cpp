#include <bits/stdc++.h>
using namespace std;

int main()
{
    long int n;
    cin >> n;
    long int a[n];
    for(long int x=0; x<n ; x++){
        cin >> a[x];
    }
  
    long int count = 0;

   for(long int i=0; i<(n-1); i++){
       if(a[i]>a[i+1]) {
           count = count + a[i]-a[i+1];
           a[i+1] = a[i];
       }
       else continue;
   }
   
    cout << count;
}
