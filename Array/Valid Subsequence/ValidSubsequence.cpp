// Subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.
// Write a function that takes in two non-empty arrays of integers and determines whether the second array is a subsequence of the first one.

#include <bits/stdc++.h>
using namespace std;

// Time Complexity: O(n) | Space Complexity: O(1)
bool isValidSubsequence(vector<int> array, vector<int> sequence)
{
    // Write your code here.
    int i = 0;
    int j = 0;
    while (i < array.size() && j < sequence.size())
    {
        if (array[i] == sequence[j])
        {
            j++;
        }
        i++;
    }
    return j == sequence.size();
}

int main()
{
    vector<int> array = {5, 1, 22, 25, 6, -1, 8, 10};
    vector<int> sequence = {1, 6, -1, 10};
    cout << isValidSubsequence(array, sequence);
    return 0;
}
// Output: 1 (True)
