#include <iostream>
using namespace std;

int grid[7][7];
string stng = "";
int solve(string mv, int x, int y)
{
    if(x==0&&y==6)
    {
        if(mv.length()==48)
        {
            bool founder = true;
            for(int i=0;i<48;i++)
            {
                if(stng[i]!=mv[i]&&stng[i]!='?'){ founder=false; break;}
            }
            if(founder) return 1;
            else return 0;
        }
        else return 0;
    }
    int count = 0;
    if(mv.length()!=0 && !(stng[mv.length()-1]=='?' || stng[mv.length()-1]== mv[mv.length()-1])) return 0;
    if(0<x&&x<6 && 0<y&&y<6 && ((grid[y-1][x]==grid[y+1][x]&&grid[y+1][x]==0 && grid[y][x-1]==grid[y][x+1]&&grid[y][x+1]==1) || (grid[y-1][x]==grid[y+1][x]&&grid[y+1][x]==1 && grid[y][x-1]==grid[y][x+1]&&grid[y][x+1]==0))) 
        return 0;
    else if((0<x&&x<6 && grid[y][x-1]==grid[y][x+1]&&grid[y][x+1]==0 &&grid[(y==0?1:5)][x]==1/*&& grid[y-abs(y-3)/(y-3)][x]==1)*/) || (0<y&&y<6 && grid[y+1][x]==grid[y-1][x]&&grid[y-1][x]==0 && grid[y][(x==0?1:5)]==1 /*&& grid[y][x-abs(x-3)/(x-3)]==1*/)) 
        return 0;

    if(y!=6 && grid[y+1][x]!=1)
    {
        grid[y+1][x]=1;
        mv.append("D");
        count+=solve(mv, x, y+1);
        mv.erase(mv.length()-1);
        grid[y+1][x]=0;
    }
    if (y!=0 && grid[y-1][x]!=1)
    {
        grid[y-1][x]=1;
        mv.append("U");
        count+=solve(mv, x, y-1);
        mv.erase(mv.length()-1);
        grid[y-1][x]=0;
    }
    if (x!=6 && grid[y][x+1]!=1)
    {
        grid[y][x+1]=1;
        mv.append("R");
        count+=solve(mv, x+1, y);
        mv.erase(mv.length()-1);
        grid[y][x+1]=0;
    }
    if(x!=0 && grid[y][x-1]!=1)
    {
        grid[y][x-1]=1;
        mv.append("L");
        count+=solve(mv, x-1, y);
        mv.erase(mv.length()-1);
        grid[y][x-1]=0;
    }
    return count;

}


int main()
{
    for(int i=0; i<7; i++)
    {
        for(int j=0; j<7; j++)
        {
            grid[i][j]=0;
        }
    }
    grid[0][0]=1;
    cin>>stng;

    cout<<solve("", 0, 0);
    return 0;
}