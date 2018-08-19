// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A)
{
  // write your code in C++14 (g++ 6.2.0)
  int minIndex = 0;
  double minAvg = (double)(A[0] + A[1]) / 2;
  for (int i = 0; i < (int)A.size() - 1; i++)
  {
    double avgOfTwo = (double)(A[i] + A[i + 1]) / 2;
    double avgOfThree = (double)(A[i] + A[i + 1] + A[i + 2]) / 3;
    if (avgOfTwo < minAvg)
    {
      minIndex = i;
      minAvg = avgOfTwo;
    }
    if (avgOfThree < minAvg and i + 2 < (int)A.size())
    {
      minIndex = i;
      minAvg = avgOfThree;
    }
  }
  return minIndex;
}