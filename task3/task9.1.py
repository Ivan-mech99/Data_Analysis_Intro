from copy import deepcopy as dp


class FragileDict:

    def __init__(self, data=dict()):
        self._data = dp(data)
        self._lock = True

    def __setitem__(self, key, item):
        if self._lock is True:
            raise RuntimeError("Protected state")
        else:
            self._data[key] = item

    def __getitem__(self, key):
        if self._lock is True:
            return dp(self._data[key])
        else:
            return self._data[key]

    def __contains__(self, key):
        if key in self._data:
            return True
        else:
            return False

    def __enter__(self):
        self.saved_data = dict()
        self.saved_data = dp(self._data)
        self._lock = False
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self._data = self.saved_data
            print("Exception has been suppressed.")
        if self._data != self.saved_data:
            self._data = dp(self._data)
        else:
            self._data = self.saved_data
        del self.saved_data
        self._lock = True
        return True
