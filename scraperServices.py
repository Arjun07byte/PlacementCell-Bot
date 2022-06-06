from time import time
import threading
import logging

logger = logging.getLogger()
prefLogger = logging.getLogger("performance")

class Service:
    def __init__(self, updateInterval, logPerf=True):
        threading.Thread.__init__(self)
        self._updateInterval = updateInterval
        self._logPerf = logPerf
    
    def runService(self):
        lastTime = -1
        while True:
            currWaitTime = lastTime + self._updateInterval - time.time()
            if currWaitTime > 0:
                time.sleep(currWaitTime)

            try:
                startTime = time.time()
                self.doGivenService()
                if self._logPerf:
                    prefLogger.info("service: {:.3f}s".format(time.time()-startTime))
            except Exception as exceptionRaised:
                logger.critical('Run error %s', exceptionRaised, exc_info=True)

    def doGivenService():
        pass