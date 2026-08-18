
#define vvi vector<vector<int>>
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
       sort(intervals.begin(), intervals.end());
        vvi output;
        output.push_back(intervals[0]);

        //test output
        cout << intervals[0][0] << " " << intervals[0][1] << "\n";
       for (auto& interval : intervals) {
        int start = interval[0];
        int end = interval[1];
        int lastEnd = output.back()[1];

        if (start <= lastEnd){
            output.back()[1] = max(lastEnd, end);
        }
        else{
            output.push_back({start,end});
        }
       } 

       return output;
    }
};
