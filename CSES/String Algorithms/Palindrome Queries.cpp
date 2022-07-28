#include <iostream>
using namespace std;

bool checkPal(string s,int a, int b)
{
    while(b>=a)
    {
        if(s[a-1]!=s[b-1])
            return false;
        a++;
        b--;
    }
    return true;
}
int main()
{
    int n,m;
    string s;
    cin>>n>>m;
    cin>>s;
    int p[m], q[m], r[m];
    char ch;
    for(int i=0;i<m;i++)
    {
        //char ch;
        cin>>p[i]>>q[i];
        if(p[i]==2) 
        cin>>r[i];
        else 
        {cin>>ch; r[i]=ch;} 
    }
    for(int i=0;i<m;i++)
    {
        if(p[i]==1)
            s[q[i]-1]=char(r[i]);
        else if(p[i]==2)
            cout<<(checkPal(s,q[i],r[i])?"YES":"NO")<<endl;
    }
}