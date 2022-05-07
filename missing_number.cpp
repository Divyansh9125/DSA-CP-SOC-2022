#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    long int n; // taking input for number of integers
    cin >> n;
    long int ain[n-1]; 
    // taking input array
    for(long int i=0; i<(n-1); i++){
        cin >> ain[i];
    }
    long int ip[n]; // defining array of positive integrs
    for(long int i=0; i<n; i++){
        ip[i] = i + 1 ;
    }
    sort(ain, ain + (n-1));
    

    
    long int mis_num = 0;
    // loop to find missing number
    for(long int j=0; mis_num == 0; j++){
        if(ain[j]==ip[j]) continue;
        else mis_num=ip[j];
    }
      cout << mis_num; 
}
