from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize two queues to simulate a stack.
        """
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto the stack.
        :param x: Element to add to the stack
        """
        self.queue2.append(x)

        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """
        Remove and return the top element of the stack.
        :return: The top element of the stack
        """
        if self.queue1:
            return self.queue1.popleft()

    def top(self) -> int:
        """
        Get the top element of the stack.
        :return: The top element of the stack
        """
        if self.queue1:
            return self.queue1[0]

    def empty(self) -> bool:
        """
        Check if the stack is empty.
        :return: True if the stack is empty, False otherwise
        """
        return not self.queue1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()