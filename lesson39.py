import time


class Timer:

    def __init__(self, elapsed_time=0, start=0, end=0):
        self.elapsed_time = elapsed_time
        self.start = start
        self.end = end

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        result = self.end - self.start
        self.elapsed_time += round(result)

    def reset(self):
        self.start = 0
        self.end = 0
        self.elapsed_time = 0


with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 секунда

time.sleep(1)
with t:
    time.sleep(2)
print(t.elapsed_time)  # ~3 секунди

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 секунда
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 секунди
