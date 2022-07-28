#include <iostream>
#include <vector>
using namespace std;

int main()
{
    string str;
    cin>>str;
    int n = str.length();
    vector <int> arr[26], count;
    for(int i=0;i<n;i++)
    {
        arr[str[i]-'a'].push_back(i);
    }
    int start = 0;
    for(int i=0;i<26;i++)
        if(arr[i].size()>0)
        {
            start = i;
            break;
        }
    count = arr[start];
    string list[count.size()];
    for(unsigned int i=0;i<count.size();i++)
        list[i]=str.substr(count[i], n).append(str.substr(0,count[i]));
    string min = list[0];
    for(unsigned int i=0;i<count.size();i++)
        if(list[i]<min) min = list[i];
    cout<<min;
}