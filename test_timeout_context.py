from timeout_context import TimeoutContext, TimeoutException
import time
import unittest

def func(sleep_s):
    time.sleep(sleep_s)

class TimeoutContextTest(unittest.TestCase):
    def test_with_timeout(self):
        timeout_context = TimeoutContext(timeout_s=3)

        with self.assertRaises(TimeoutException):
            with timeout_context:
                func(3.1)

    def test_without_timeout(self):
        timeout_context = TimeoutContext(timeout_s=3)

        with timeout_context:
            func(2.9)


if __name__ == '__main__':
    unittest.main()

