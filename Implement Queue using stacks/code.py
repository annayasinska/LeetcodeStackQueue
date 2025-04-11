class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []
        

    def push(self, x: int) -> None:
        self.a.append(x)
        

    def pop(self) -> int:
        self._move_a_to_b()
        return self.b.pop()
        

    def peek(self) -> int:
        self._move_a_to_b()
        return self.b[-1]
        

    def empty(self) -> bool:
        return not self.a and not self.b
        
    def _move_a_to_b(self) -> None:
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()