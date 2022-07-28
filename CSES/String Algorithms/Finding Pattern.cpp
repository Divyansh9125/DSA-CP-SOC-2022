#include <iostream>
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
bool KMP(string pat, string txt)
{
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
            return true;
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
    return false;
}
int main()
{
    string s;
    cin>>s;
    int n;
    cin>>n;
    string word[n];
    for (int i = 0; i < n; i++)
    {
        cin>>word[i];
    }
    for (int i = 0; i < n; i++)
    {
        cout<<(KMP(word[i],s)?"YES":"NO")<<endl;
    }

}