#include<iostream>
#include<cmath>
using namespace std;
int countdigits(int x){
int count=0;
while(x>0){
x=x/10;
count++;
}
return count;
}