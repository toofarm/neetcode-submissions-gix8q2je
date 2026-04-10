class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_val = min(val, self.ordered[len(self.ordered) - 1]) if len(self.ordered) > 0 else val
        self.ordered.append(min_val)

        # print('push')
        # print(self.stack)

    def pop(self) -> None:
        self.ordered.pop(len(self.stack) - 1)
        self.stack.pop(len(self.stack) - 1)

        # print('pop - self.stack')
        # print(self.stack)
        # print('pop - self.ordered')
        # print(self.ordered)

    def top(self) -> int:
        # print('top')
        # print(self.stack)
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        # print('getMin - self.ordered')
        # print(self.ordered)
        return self.ordered[len(self.ordered) - 1]
