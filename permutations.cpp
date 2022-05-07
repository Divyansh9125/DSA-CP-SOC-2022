#include <iostream>
using namespace std;

int main(){
   long int n;
   cin >> n;
   long int a[n];
   for(long int i =0; i<(n/2) ;i++){
       a[i] = n-1- 2*i;
   }
   for(long int j = 0; j<(n/2 +1) ; j++){
       a[n/2 + j] = n -2*j;
   }
   if (n==2 || n==3) cout<<"NO SOLUTION";
   else{
       for(long int x=0; x<n; x++){
           cout << a[x] << " ";
       }
   }
   
}
