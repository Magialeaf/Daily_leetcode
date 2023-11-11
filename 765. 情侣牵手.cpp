class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        int n = row.size();
        int ans = 0;

        unordered_map<int, int> pos;
        for (int i = 0; i < n; i++) {
            pos[row[i]] = i;
        }

        for (int i = 0; i < n; i += 2) { 
            int x = row[i];
            if (row[i + 1] == (x ^ 1)) { 
                continue;
            }
            int y = (x % 2 == 0) ? (x + 1) : (x - 1);
            int idx = pos[y];
            swap(row[i + 1], row[idx]);
            pos[row[i + 1]] = i + 1;
            pos[row[idx]] = idx;
            ans++;
        }
        return ans;

    }
};