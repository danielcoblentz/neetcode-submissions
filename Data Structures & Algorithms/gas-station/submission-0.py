'''
input: n stations in a circle, 2 arrays 
    gas[i] = amt of gas at position i
    cost[i] = amt of gas needed to get to the next station i -> i +1
    * last is connected to first


output: the idx of starting station st we can make an entire trip, if impossible -1
edge cases: empty input, not possible, types of inputs proided (str, int, empty values, diff lengths)

notes / questions:
1) is there a case where its not the best option to start at the max val of the gas?
2) we need some way to incrmeent the count of stations we can visit if that is == to len(input) we have made it but we need to do some wokr before we can incrmeent the result
or if we use hte idx as the starting value and each tur nwe decrement if we get 0 then we are good

init --> count to track the number of stations visited
record starting idx so we know if from there it is possible

iterate though the len of g or c (assuming the same length)
amt_fuel += g[i]
amt_fuel -= c[i]

if c[i] > g[i] then its not possible we skip it and reset
'''

class Solution:


    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost): return -1

        current_fuel = 0
        start_idx = 0
        for i in range(len(gas)):
            current_fuel += gas[i] - cost[i]
            if current_fuel < 0:
                start_idx = i + 1
                current_fuel = 0


                
        return start_idx



        