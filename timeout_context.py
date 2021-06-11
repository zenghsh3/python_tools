import signal

class TimeoutException(Exception):
    def __str__(self):
        return "timeout exception."

def handler(signum, frame):
    raise TimeoutException()

class TimeoutContext(object):
    def __init__(self, timeout_s):
        """ Only supported in UNIX

        Args:
            timeout_s(int): seconds of timeout limit
        """
        assert isinstance(timeout_s, int)
        signal.signal(signal.SIGALRM, handler)
        self.timeout_s = timeout_s

    def __enter__(self):
        signal.alarm(self.timeout_s)

    def __exit__(self, type, value, tb):
        # Cancel the timer if the function returned before timeout
        signal.alarm(0)
