#include<iostream>
using namespace std;
int fun(int n)
{
     if(n<=1) return 1;
     return n*fun(n-1);	 	
}
int main()
{
	int n;
	cout<<"enter n:";
	cin>>n;
	cout<<"n="<<n;
	return 0;
	
}
