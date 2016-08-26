#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t,n;
    cin>>t;
    while(t--)
        {
        cin>>n;
        vector<int >stocks(n);
        long long sum=0;
        for (int i=0;i<n;i++)
            {
            cin>>stocks[i];
        }
        int max=stocks[n-1];
        for(int i=n-2;i>=0;i--)
            {
            if(max>stocks[i])
                {
                sum+=max-stocks[i];
            }
            else if(max<stocks[i])
                {
                max=stocks[i];
            }

        }
        cout<<sum<<endl;
        stocks.clear();
    }
    return 0;
}
