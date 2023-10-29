class Solution {
public:
	int hIndex(vector<int>& citations) {
		int maxs = INT_MIN;
		int mins = INT_MAX;
		for (int i = 0; i < citations.size(); i++)
		{
			if (citations[i] > maxs)
			{
				maxs = citations[i];
			}
			if (citations[i] < mins)
			{
				mins = citations[i];
			}
		}

		vector<int> countArr(maxs - mins + 1, 0);
		for (int i = 0; i < citations.size(); i++)
		{
			countArr[citations[i] - mins]++;
		}

		int res = 0;
		for (int i = maxs - mins; i >= 0; i--)
		{
			if (i + mins >= res + countArr[i])
			{
				res += countArr[i];
			}
			else
			{
                res = max(res,i + mins);
				break;
			}
		}
		return res;
	}
};