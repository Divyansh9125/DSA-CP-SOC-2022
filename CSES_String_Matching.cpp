#include <iostream>
#include <string>
using namespace std;

// Using KMP Algorithm

void fillLPS(const string &str, int lps[])
{
    int n=str.length(),len=0,i=1;
    lps[0]=0;
    while(i<n)
    {
        if(str[i]==str[len])
        {
            len++;
            lps[i++]=len;
        }
        else
        {
            if(len==0)
            lps[i++]=0;
            else
            len=lps[len-1];
        }
    }
}

int KMP(const string &txt,const string &pat)
{
    int n=txt.length();
    int m=pat.length();
    int lps[m];
    fillLPS(pat,lps);
    int i=0,j=0,count=0;
    while(i<n)
    {
        if(pat[j]==txt[i])
        {
            i++;
            j++;
        }
        if(j==m)
        {
            count++;
            j=lps[j-1];
        }
        else if(i<n && pat[j]!=txt[i])
        {
            if(j==0)
            i++;
            else
            j=lps[j-1];
        }
    }
    return count;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string txt,pat;
    cin>>txt;
    cin>>pat;
    cout<<KMP(txt,pat)<<"\n";
    return 0;
}