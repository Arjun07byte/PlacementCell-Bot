from time import time
import threading


class Service(threading.Thread):
    def __init__(self, updateInterval):
        threading.Thread.__init__(self)
        self._updateInterval = updateInterval
    
    def run(self):
        lastTime = -1
        while True:
            currWaitTime = lastTime + self._updateInterval - time()
            if currWaitTime > 0:
                time.sleep(currWaitTime)

            try:
                self.doGivenService()
            except Exception as exceptionRaised:
                # handle exception raised here
                pass

    def doGivenService(self):
        pass