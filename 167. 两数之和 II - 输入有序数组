class Solution
{
public:
	vector<int> twoSum(vector<int>& numbers, int target)
	{
		vector<int> res;
		res.push_back(0);
		res.push_back(numbers.size() - 1);
		while (numbers[res[0]] + numbers[res[1]] != target)
		{
			if (numbers[res[0]] + numbers[res[1]] > target)
			{
				res[1] -= 1;
			}
			else
			{
				res[0] += 1;
			}
		}
		res[0] += 1;
		res[1] += 1;
		return res;
	}
};