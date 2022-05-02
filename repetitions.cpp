#include<iostream>
#include<cmath>
using namespace std;
int main(){
    string dna;
    cin>>dna;
    int c=1;
    int rep=1;
    for(int i=0;i<dna.length()-1;i++){
if(dna[i]==dna[i+1]) c++; else c=1;
rep=max(rep,c);
    }
    cout<<rep;
}