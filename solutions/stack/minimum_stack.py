class MinStack:

    def __init__(self):
        self.s = []
        self.minS = []

    def push(self, val: int) -> None:
        self.s.append(val)
        val = min(val,self.minS[-1] if self.minS else val)
        self.minS.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minS[-1]
