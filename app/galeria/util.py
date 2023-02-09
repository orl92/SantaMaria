class _Skip:
    def __init__(self, now, next, previous):
        self.__now, self.__next, self.__previous = now, next, previous

    @property
    def now(self):
        return self.__now

    @property
    def next(self):
        return self.__next

    @property
    def previous(self):
        return self.__previous
