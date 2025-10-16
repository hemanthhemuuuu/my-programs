#include<iostream>
using namespace std;

class Std {
    int id;
    char name;
    double cgpa;
public:
    void get() {
        cout << "Enter ID: ";
        cin >> id;

        cout << "Enter Name (single character): ";
        cin >> name;

        cout << "Enter CGPA: ";
        cin >> cgpa;
    }

    double getCgpa() {
        return cgpa;
    }

    void display() {
        cout << "ID: " << id << endl;
        cout << "Name: " << name << endl;
        cout << "CGPA: " << cgpa << endl;
    }
};


int max(Std s[], int n) {
    int maxIndex = 0;
    for (int i = 1; i < n; i++) {
        if (s[i].getCgpa() > s[maxIndex].getCgpa()) {
            maxIndex = i;
        }
    }
    return maxIndex;
}

int main() {
    int n;
    cout << "Enter number of students: ";
    cin >> n;

    Std s[100];

    for (int i = 0; i < n; i++) {
        cout << "\n--- Enter details for student " << i + 1 << " ---" << endl;
        s[i].get();
    }

    int maxIndex = max(s, n);

    cout << "Student with Maximum CGPA =====" << endl;
    s[maxIndex].display();

    return 0;
}

