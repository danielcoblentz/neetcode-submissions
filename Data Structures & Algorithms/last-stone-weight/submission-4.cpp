class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int>maxH = {stones.begin(), stones.end()};

        while(maxH.size() > 1){
            //get two stones from top
            int stone1 = maxH.top();
            maxH.pop();
            int stone2 = maxH.top();
            maxH.pop();

            if (stone1 != stone2){
                maxH.push(abs(stone1 - stone2));
            }
        }
        if (!maxH.empty()){ return maxH.top();}
        else{return 0;}
    }
};
