class Gate:
    def __init__(self, state=False):
        self._state = bool(state)

    def state(self):
        return self._state

    def switch(self):
        self._state = not self._state
        return self

    def off(self):
        self._state = False
        return self

    def on(self):
        self._state = True
        return self

    def set(self, state: bool):
        self._state = bool(state)
        return self

    def switchIF(self, condition: bool):
        if condition:
            self._state = not self._state
        return self

    def offIF(self, condition: bool):
        if condition:
            self._state = False
        return self

    def onIF(self, condition: bool):
        if condition:
            self._state = True
        return self

    def setIF(self, state: bool, condition: bool):
        if condition:
            self._state = bool(state)
        return self

    def __bool__(self):
        return self._state

    def __int__(self):
        return int(self._state)

    def __float__(self):
        return float(self._state)

    def __str__(self):
        return str(self._state)

    def __repr__(self):
        return f' -> {self._state} -> '
