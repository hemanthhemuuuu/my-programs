#include<iostream>
using namespace std;

class cse6 {
    int i;
public:
    void set1(int n) { i = n; }
    int get1() { return i; }
};

cse6 newfun() {
    cse6 x;
    x.set1(10); 
    return x;
}

int main() {
    cse6 obj;
    obj = newfun(); 
    cout << "Now we are in main....printing i = " << obj.get1() << endl;
    return 0;
}

