#include <bits/stdc++.h>
using namespace std;

// O(n^2) time | O(1) space
vector<int> twoNumberSumN2(vector<int> array, int targetSum)
{
    // Write your code here.
    vector<int> result;
    for (int i = 0; i < array.size(); i++)
    {
        for (int j = i + 1; j < array.size(); j++)
        {
            if (array[i] + array[j] == targetSum)
            {
                result.push_back(array[i]);
                result.push_back(array[j]);
                return result;
            }
        }
    }
    return result;
}
// O(n) time | O(n) space
vector<int> twoNumberSumN(vector<int> array, int targetSum)
{
    // Write your code here.
    vector<int> result;
    unordered_set<int> s;
    for (int i = 0; i < array.size(); i++)
    {
        int x = targetSum - array[i];
        if (s.find(x) != s.end())
        {
            result.push_back(x);
            result.push_back(array[i]);
            return result;
        }
        s.insert(array[i]);
    }
    return result;
}
// O(nlogn) time | O(1) space
vector<int> twoNumberSumNlogN(vector<int> array, int targetSum)
{
    // Write your code here.
    vector<int> result;
    sort(array.begin(), array.end());
    int left = 0;
    int right = array.size() - 1;
    while (left < right)
    {
        int currentSum = array[left] + array[right];
        if (currentSum == targetSum)
        {
            result.push_back(array[left]);
            result.push_back(array[right]);
            return result;
        }
        else if (currentSum < targetSum)
        {
            left++;
        }
        else if (currentSum > targetSum)
        {
            right--;
        }
    }
    return result;
}

int main()
{
    vector<int> array = {3, 5, -4, 8, 11, 1, -1, 6};
    int targetSum = 10;
    vector<int> result = twoNumberSumNlogN(array, targetSum);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
    return 0;
}