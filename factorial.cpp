#include<iostream>
#include<cmath>
using namespace std;
int fac(int x){
if(x==0) {return 1;}
return x*fac(x-1);
}