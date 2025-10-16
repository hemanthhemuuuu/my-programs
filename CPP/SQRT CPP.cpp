#include<iostream>
using namespace std;
int main()
{
	int a,b,c,root;
    cout<<"enter a :""\n"<<"enter b :""\n""enter c :";
    cin>>a>>b>>c;
    root=-b+sqrt(b*b-4*a*c)/2*a;
    cout<<"root="<<root;
    return 0;
}
