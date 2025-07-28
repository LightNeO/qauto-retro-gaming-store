"""
Timer helper for performance testing
"""

import time


class TimerHelper:

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        """Stop the timer and return elapsed time in milliseconds"""
        if self.start_time is None:
            raise Exception("Timer was not started. Call start() before stop().")

        self.end_time = time.time()
        elapsed_seconds = self.end_time - self.start_time
        return elapsed_seconds * 1000

    def get_elapsed_time(self):
        """Get elapsed time in milliseconds"""
        if self.start_time is None:
            return 0
        if self.end_time is None:
            return (time.time() - self.start_time) * 1000
        return (self.end_time - self.start_time) * 1000

    def reset(self):
        """Reset timer to initial state"""
        self.start_time = None
        self.end_time = None
