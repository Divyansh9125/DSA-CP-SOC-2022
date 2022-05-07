#include <iostream>
using namespace std;
int main(){
    long int n;
    cin >> n;
   long int count=0;
    
    while(n!=0){
        n = n/5;
        count = count + n;
    }
    cout << count;
}