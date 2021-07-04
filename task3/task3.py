import signal
import functools


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def handler(signum, frame):
    raise TimeoutException("Timed out")


def timeout(seconds):
    def signalization(func):
        if seconds is None or seconds <= 0:
            return func

        @functools.wraps(func)
        def wrapper(*args, **argv):
            signal.signal(signal.SIGALRM, handler)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                res = func(*args, **argv)
            except Exception as e:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, signal.SIG_DFL)
                raise e
            signal.alarm(0)
            signal.signal(signal.SIGALRM, signal.SIG_DFL)
            return res
        return wrapper
    return signalization
