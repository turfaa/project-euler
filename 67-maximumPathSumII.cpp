/* Author : Turfa Auliarachman
 * Just a little modification from the 18-maximumPathSumI.cpp*/

#include <bits/stdc++.h>
using namespace std;
const int n = 100;
const string nama = "67-maximumPathSumII.txt";

int memo[n+10][n+10];
int number[n+10][n+10];

int dp(int x, int y){
    int &mem = memo[x][y];

    if (x==n-1) return number[x][y];
    else if (mem>-1) return mem;
    else return mem = number[x][y] + max(dp(x+1,y), dp(x+1,y+1));
}

int main(){
    fstream inp;
    inp.open(nama.c_str());
    
    memset(memo,-1,sizeof memo);

    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            inp >> number[i][j];
        }
    }
    inp.close();

    cout << dp(0,0) << endl;
    return 0;
}
