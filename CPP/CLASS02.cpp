#include<iostream>
using namespace std;

class h {
private:
    int rono;
    char name[20];

public:
    void get() {
        cout << "Enter roll no.: ";
        cin >> rono;
        cout << "Enter name: ";
        cin >> name;
    }

    void show() {
        cout << "Roll No.: " << rono << endl;
        cout << "Name: " << name << endl;
    }
};

int main() {
    int n;
    cout << "Enter number of students: ";
    cin >> n;

    h s[100];  // Array of objects (maximum 100 students)

    for (int i = 0; i < n; i++) {
        cout << "\nEnter details for student " << i + 1 << ":\n";
        s[i].get();
    }

    cout << "\n--- Student Details ---\n";
    for (int i = 0; i < n; i++) {
        cout << "\nDetails of student " << i + 1 << ":\n";
        s[i].show();
    }

    return 0;
}

