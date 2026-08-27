class MinStack:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.temp:
            self.temp.append(val)
        else:
            current_min = self.temp[-1]
            self.temp.append(min(current_min, val))

    def pop(self) -> None:
        self.stack.pop()
        self.temp.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.temp[-1]
        
