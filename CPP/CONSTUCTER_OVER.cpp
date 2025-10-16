#include<iostream>
using namespace std;

class A {
    int a;

public:
    A() {
        a = 10;
        cout << "Default constructor activated" << endl;
    }

    A(int b) {
        a = 10 + b; // Assuming you wanted to add b to initial a=10
        cout << "a value: " << a << endl;
    }

    A(int x, double y) {
        cout << "x = " << x << endl;
        cout << "y = " << y << endl;
    }

    A(double k, int s) {
        cout << "k = " << k << endl;
        cout << "s = " << s << endl;
    }
};

int main() {
    A obj1;
    A obj2(20);
    A obj3(10, 20.5);   // Make sure second param is double
    A obj4(40.5, 50);   // Make sure first param is double

    return 0;
}

