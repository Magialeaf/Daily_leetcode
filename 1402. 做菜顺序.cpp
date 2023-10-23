class Solution {
public:
	int maxSatisfaction(vector<int>& satisfaction) {
		sort(satisfaction.begin(), satisfaction.end());
		int p = 0;

		for (int i = 0; i < satisfaction.size(); i++)
		{
			if (satisfaction[i] >= 0)
			{
				p = i;
				break;
			}
		}

		int lp = p - 1;
		int rp = p;
		if (satisfaction[rp] < 0)
		{
			return 0;
		}

		int level = 1;
		int sum = 0;
		int sum_temp = 0;
		while (rp < satisfaction.size())
		{
			sum += level * satisfaction[rp];
			sum_temp += satisfaction[rp];
			level++;
			rp++;
		}

		int sub = 0;
		int sub_temp = 0;
		int res = sum;
		while (lp >= 0)
		{
			sub_temp = satisfaction[lp] + sub_temp;
			sub += sub_temp;
			sum += sum_temp;
			if (res < sum + sub)
			{
				lp--;
				res = sum + sub;
			}
			else
			{
				break;
			}
		}

		return res;
	}
};