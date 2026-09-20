class KthLargest {
private:
priority_queue<int, vector<int>, greater<int>> minH;
int k;


public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            minH.push(num);
            if (minH.size() > k) {
                minH.pop();
            }
        }
        
    }
    
    int add(int val) {
        minH.push(val);
        if (minH.size() > k) {
            minH.pop();
        }
        return minH.top();
    }
};
