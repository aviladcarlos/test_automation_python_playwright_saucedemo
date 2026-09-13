import time

class BaseClass:

    def __init__(self):
        self.startime = None
        self.endtime = None
        self.overalltime = None

    def timer_start(self):
        self.startime = time.time()

    def timer_end(self):
        self.endtime = time.time()

    def timer_overall_seconds(self):
        self.overalltime = self.endtime - self.startime
        return time.localtime(self.overalltime).tm_sec
