#include <iostream>
using namespace std;

int plusFuncInt(int x, int y) {
  return x + y;
}

int plusFuncInt(int x, int y, int j) {
  return x + y + j;
}

int main() {
  int myNum1 = plusFuncInt(8, 5); // with two number
  double myNum2 = plusFuncInt(4, 6, 7); // with three number
  cout << "Int: " << myNum1 << "\n";
  cout << "Double: " << myNum2;
  return 0;
}