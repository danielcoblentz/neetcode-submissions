'''
input: some number of function calls to the class we need to support
want: a way to get each function to run i O(1) time. so we canot run min(stack) to return hte smallest element at any point in time

edge case: none atm

time, space - 
exp:
we use two stacks one will be for supporting hte following:
    - push
    - pop
    - top
the second stack will trakc hte currnt minimum at any point in time every time we push a val we check if it is smaller than hte prev
if it is we append it to the top so each element 

s1 = [1,2,0]
s2 = [1,1,0]

s2 tracks min at every point in time
this is what will support getMin in O(1) because we are just getting hte top eleement at that point in time











'''









class MinStack:

    def __init__(self):
       self.s1 = []
       self.s2 = [] 

    def push(self, val: int) -> None:
        self.s1.append(val)
        if not self.s2:
            self.s2.append(val)
        elif self.s2[-1] < val:
            self.s2.append(self.s2[-1])
        else:
            self.s2.append(val)


    def pop(self) -> None:
        if self.s1: self.s1.pop()
        if self.s2: self.s2.pop()

    def top(self) -> int:
        return self.s1[-1] if self.s1 else 0

    def getMin(self) -> int:
        return self.s2[-1] if self.s2 else 0
