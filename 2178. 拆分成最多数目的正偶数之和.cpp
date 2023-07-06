class Solution {
public:
    vector<long long> maximumEvenSplit(long long finalSum) {
        long long last = 2;
        vector<long long> res;
        if(finalSum % 2 == 1)
        {
            return res;
        }
        else
        {
            while (last <= finalSum)
            {
                res.push_back(last);
                finalSum -= last;
                last += 2;
            }
            res[res.size() - 1] += finalSum;
            return res;
        }
    }
};
