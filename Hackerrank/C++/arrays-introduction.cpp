#include <iostream>
using namespace std;


int main() {
    int n; cin >> n;
    int arr[n], num;
    for (int i=0; i<n; i++) {
        cin >> num;
        arr[i] = num;
    }
    for (int i=n-1; i>=0; i--)
        cout << arr[i] << ' ';
    return 0;

}
