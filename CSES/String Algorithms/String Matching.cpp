#include <iostream>
#include <vector>

using namespace std;

void computeLPS(string pat, int m, int* lps)
{
    int len  = 0;
    lps[0]=0;
    int i = 1;
    while (i < m) 
    {
        if (pat[i] == pat[len]) {
            len++;
            lps[i] = len;
            i++;
        }
        else
        {
            if(len!=0)
            {
                len = lps[len-1];
            }
            else{
                lps[i]=0;
                i++;
            }
        }
    }
}
int KMP(string pat, string txt)
{
    int res =0;
    int m = pat.length(), n = txt.length(), lps[m];
    computeLPS(pat, m, lps);
    int i = 0, j=0;
    while(i<n)
    {
        if(pat[j]==txt[i])
        {
            i++;
            j++;
        }
        if(j==m)
        {
            res++;
            j = lps[j-1];
        }
        else if(i<n && pat[j] !=txt[i])
        {
            if (j != 0)
                j = lps[j - 1];
            else
                i = i + 1;
        }
    }
    return res;
}

int main()
{

    string s, p;
    cin>>s>>p;
    cout<<KMP(p,s);
}