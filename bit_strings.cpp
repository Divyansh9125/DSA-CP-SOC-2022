#include <iostream>
using namespace std;
#define ll long long
#define mod (ll)(1e9 + 7)
// An iterative function to find (x^y)%p in O(log y)
ll power(ll x, ll y, ll p){
   ll result = 1;
   x = x % p; // Update x if it is more than or
   // equal to p
   while (y > 0){
      // If y is odd, multiply x with result
      if (y & 1){
         result = (result * x) % p;
      }
      // y must be even now
      y = y >> 1; // y = y/2
      x = (x * x) % p;
   }
   return result;
}
// Function to count the number of binary strings
ll countbstring(ll num){
   int count = power(2, num, mod);
   return count;
}
int main(){
   ll num;
   cin >> num;
   cout<<countbstring(num);
   return 0;
}
