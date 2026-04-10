class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_val = min(val, self.ordered[len(self.ordered) - 1]) if len(self.ordered) > 0 else val
        self.ordered.append(min_val)

    def pop(self) -> None:
        self.ordered.pop(len(self.stack) - 1)
        self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.ordered[len(self.ordered) - 1]
