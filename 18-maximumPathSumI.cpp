/* Author : Turfa Auliarachman
 * Actually, this problem can be solved by naive method.
 * But I use Dynamic Programming here, so I can solve this problem and Problem 67 - Maximum path sum II by just one code.*/

#include <bits/stdc++.h>
using namespace std;
const int n = 15;
const string nama = "18-maximumPathSumI.txt";

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
