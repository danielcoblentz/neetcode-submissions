class MinStack:

    def __init__(self):
        self.s = []
        self.minS = []

    def push(self, val: int) -> None:
        self.s.append(val)
        new_min = min(val, self.minS[-1] if self.minS else val)
        self.minS.append(new_min)

    def pop(self) -> None:
        self.s.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minS[-1]
