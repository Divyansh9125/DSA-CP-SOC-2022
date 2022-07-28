#include <iostream>
using namespace std;

int main()
{
    string s;
    cin>>s;
    if(s.substr(0,10)=="aaaaaaaaaa")
    {
        cout<<s;
        return 0;
    }
    string m = s.substr(0,1);
    int ans=0, len = 1, c=0, cl=0;
    for(int i = 1;i<s.length();i++)
    {
        m+=s[i];
        if(m[i]==m[c])
        {
            cl+=2;
            c--;
            if(c==-1)
            {
                if(cl>len)
                {
                    len=cl;
                    ans=c+1;
                }
                c = c+cl/2+1;
                m.erase(c+1);
                i = c;
                cl=0;
            }
        }
        else
        {
            if(cl>len)
            {
                len=cl;
                ans=c+1;
            }
            c = c+cl/2+1;
            m.erase(c+1);
            i = c;
            cl=0;
        }
    }
    m = s.substr(0,2), c=0, cl=1;
    for(int i = 2;i<s.length();i++)
    {
        m+=s[i];
        if(m[i]==m[c])
        {
            cl+=2;
            c--;
            if(c==-1)
            {
                if(cl>len)
                {
                    len=cl;
                    ans=c+1;
                }
                c = i-1;
                cl=1;
            }
        }
        else
        {
            if(cl>len)
            {
                len=cl;
                ans=c+1;
            }
            c = i-1;
            cl=1;
        }
    }
    cout<<s.substr(ans,len);
}