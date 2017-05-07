import timeit, random, math, signal, logging
import numpy as np


class TimeoutException(Exception):  # Custom exception class
    pass


class Complexity:
    def createLogger(self):
        logger = logging.getLogger("logger")
        logger.setLevel(logging.INFO)
        handle = logging.FileHandler("forTesting/test.log")
        logger.addHandler(handle)
        return logger


    def __init__(self, code, setup):
        with open(code, 'r') as myfile:
            self._code = myfile.read().replace('\n', ';')
        with open(setup, 'r') as myfile:
            self._setup = myfile.read().replace('\n', ';')
        self._vals = []
        self._valsx = []

    def complexityClass(self):

        def timeout_handler(signum, frame):
            raise TimeoutException


        global x
        x = 10000
        final = 0
        logger = self.createLogger()
        signal.alarm(30)
        try:
            for i in range(7):
                timer = timeit.Timer(self._code, self._setup, globals=globals())
                self._vals.append(timer.timeit(1))
                self._valsx.append(x)
                x *= 2
        except TimeoutException:
            logger.exception("bigger than O(n)")
            print("failed")


        for i in range(1, 5):
            final += (self._vals[i]/self._vals[i-1])
        ratio = math.floor(final/4*10)/10
        print(ratio)
        if ratio < 1.5:
            print("Estimated Complexity: O(1)")
        elif ratio < 2.2:
            print("Estimated Complexity: O(n)")
        elif ratio < 2.6:
            print("Estimated Complexity: O(nlogn)")
        elif ratio > 2.5:
            print("Estimated Complexity: O(n^2)")


    def timeInData(self, data):
        z = np.polyfit(self._valsx, self._vals, 1)
        p = np.poly1d(z)
        print(p(data))

    def dataInTime(self, time):
        z = np.polyfit(self._vals, self._valsx, 1)
        p = np.poly1d(z)
        print(p(time))


comp = Complexity("/home/jasiek/PycharmProjects/forTesting/code", "/home/jasiek/PycharmProjects/forTesting/setup")
comp.complexityClass()
comp.dataInTime(0.7)