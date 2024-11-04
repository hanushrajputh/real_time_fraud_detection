
from collections import deque

class SlidingWindow:
    def __init__(self, window_size):
        self.window = deque(maxlen=window_size)

    def add(self, transaction):
        self.window.append(transaction)

    def get_window_data(self):
        return list(self.window)
    