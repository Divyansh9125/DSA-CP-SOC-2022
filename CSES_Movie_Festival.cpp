#include <iostream>
#include <algorithm>
using namespace std;

// Using Greedy Algorithm for Scheduling Problem

 struct Movie
 {
    int start,finish;
 };

 bool compare(Movie m1,Movie m2)
 {
    return (m1.finish<m2.finish);
 }

 int maxMovies(Movie arr[],int n)
 {
    sort(arr,arr+n,compare);
    int i=0,count=1; // First movie will always get selected
    for(int j=1;j<n;j++)
    {
        if(arr[j].start>=arr[i].finish)
        {
            count++;
            i=j;
        }
    }
    return count;
 }
 
 int main()
 {
    int n;
    cin>>n;
    Movie arr[n];
    for(int i=0;i<n;i++)
    cin>>arr[i].start>>arr[i].finish;
    cout<<maxMovies(arr,n)<<"\n";
 }