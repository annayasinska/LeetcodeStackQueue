from collections import defaultdict


class MyQueue:
    def __init__(self):
        """
        Initialize the queue using a list.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push an element to the back of the queue.
        :param x: Element to add
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Remove and return the front element from the queue.
        :return: The front element
        """
        if not self.empty():

            return self.queue.pop(0)
        raise IndexError("pop from an empty queue")

    def peek(self) -> int:
        """
        Return the front element of the queue without removing it.
        :return: The front element
        """
        if not self.empty():
            return self.queue[0]
        raise IndexError("peek from an empty queue")

    def empty(self) -> bool:
        """
        Check if the queue is empty.
        :return: True if empty, False otherwise
        """
        return len(self.queue) == 0


class MyStack:
    def __init__(self):
        """
        Initialize the stack using a list.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push an element onto the stack.
        :param x: Element to add
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Remove and return the top (last added) element from the stack.
        :return: The top element
        """
        if not self.empty():
            return self.stack.pop()
        raise IndexError("pop from an empty stack")

    def top(self) -> int:
        """
        Return the top (last added) element without removing it.
        :return: The top element
        """
        if not self.empty():
            return self.stack[-1]
        raise IndexError("top from an empty stack")

    def empty(self) -> bool:
        """
        Check if the stack is empty.
        :return: True if empty, False otherwise
        """
        return len(self.stack) == 0


class FreqStack:
    def __init__(self):
        """
        Initialize the frequency stack using MyStack and MyQueue.
        """
        self.freq = defaultdict(int)

        self.group = defaultdict(MyStack)

        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        Push an integer val onto the stack.
        """
        self.freq[val] += 1
        freq = self.freq[val]

        self.max_freq = max(self.max_freq, freq)

        self.group[freq].push(val)

    def pop(self) -> int:
        """
        Remove and return the most frequent element in the stack.
        """
        val = self.group[self.max_freq].pop()

        self.freq[val] -= 1

        if self.group[self.max_freq].empty():
            self.max_freq -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()