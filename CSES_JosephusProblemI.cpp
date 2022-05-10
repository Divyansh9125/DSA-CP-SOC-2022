#include <iostream>
#include <list>
using namespace std;

void josephus(int n)
{
    list<int> l;
    for(int i=0;i<n;i++)
    l.push_back(i+1);
    list <int> :: iterator it;
    it=l.begin();
    while(l.size()>1)
    {
        for(int i=1;i<2;i++)
        {
            it++;
            if(it==l.end())
            it=l.begin();
        }
        cout<<*it<<" ";
        it=l.erase(it);
        if(it==l.end())
        it=l.begin();
    }
    cout<<l.front()<<endl;
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    josephus(n);
    return 0;
}